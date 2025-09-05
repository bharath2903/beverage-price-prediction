
import joblib
import pandas as pd

MODEL_PATH = "artifacts/model_data.joblib"
model_data = joblib.load(MODEL_PATH)
model = model_data["model"]
features = model_data["features"]
label_classes = model_data.get("label_classes")

def _decode_label(y_idx):

    try:
        i = int(y_idx)
    except Exception:
        return str(y_idx)
    if label_classes and 0 <= i < len(label_classes):
        return label_classes[i]
    # fallback: if model has string classes baked in
    if hasattr(model, "classes_") and len(getattr(model, "classes_", [])) and isinstance(model.classes_[0], str):
        try:
            return model.classes_[i]
        except Exception:
            pass
    return str(i)

def preprocess_input(age, gender, zone, occupation, income_levels, consume_freq,
                     current_brand, size, awareness, reasons, flavor, channel,
                     packaging, health, situation):
    # create single-row DF with all zeros in the exact model feature order
    df = pd.DataFrame(0, columns=features, index=[0])

    if zone == "Rural":
        zone_code = 1
    elif zone == "Semi-Urban":
        zone_code = 2
    elif zone == "Urban":
        zone_code = 3
    elif zone == "Metro":
        zone_code = 4
    else:
        zone_code = 0
    df.at[0, "zone"] = zone_code

    if consume_freq == "0-2 times":
        cf_code = 1
    elif consume_freq == "3-4 times":
        cf_code = 2
    elif consume_freq == "5-7 times":
        cf_code = 3
    else:
        cf_code = 0
    df.at[0, "consume_frequency(weekly)"] = cf_code

    if awareness == "0 to 1":
        aware_code = 1
    elif awareness == "2 to 4":
        aware_code = 2
    elif awareness == "above 4":
        aware_code = 3
    else:
        aware_code = 0
    df.at[0, "awareness_of_other_brands"] = aware_code

    if 18 <= age <= 25:
        age_code = 1
    elif age <= 35:
        age_code = 2
    elif age <= 45:
        age_code = 3
    elif age <= 55:
        age_code = 4
    elif age <= 70:
        age_code = 5
    else:
        age_code = 6
    df.at[0, "age_group"] = age_code

    if income_levels == "<10L":
        inc_code = 1
    elif income_levels == "10L - 15L":
        inc_code = 2
    elif income_levels == "16L - 25L":
        inc_code = 3
    elif income_levels == "26L - 35L":
        inc_code = 4
    elif income_levels == "> 35L":
        inc_code = 5
    elif income_levels == "not reported":
        inc_code = 0
    else:
        inc_code = 0
    df.at[0, "income_levels"] = inc_code

    if isinstance(health, str) and health.startswith("Low"):
        health_code = 1
    elif isinstance(health, str) and health.startswith("Medium"):
        health_code = 2
    elif isinstance(health, str) and health.startswith("High"):
        health_code = 3
    else:
        health_code = 0
    df.at[0, "health_concerns"] = health_code

    if isinstance(size, str) and size.startswith("Small"):
        size_code = 1
    elif isinstance(size, str) and size.startswith("Medium"):
        size_code = 2
    elif isinstance(size, str) and size.startswith("Large"):
        size_code = 3
    else:
        size_code = 0
    df.at[0, "preferable_consumption_size"] = size_code

    df.at[0, "cf_ab_score"] = round(aware_code / (aware_code + cf_code), 2) if (aware_code + cf_code) else 0
    df.at[0, "zas_score"] = inc_code * zone_code
    df.at[0, "bsi"] = 1 if (current_brand != "Established" and reasons in ["Price", "Quality"]) else 0

    if gender == "M" and "gender_M" in df.columns:
        df.at[0, "gender_M"] = 1

    if occupation == "Working Professional" and "occupation_Working Professional" in df.columns:
        df.at[0, "occupation_Working Professional"] = 1
    elif occupation == "Student" and "occupation_Student" in df.columns:
        df.at[0, "occupation_Student"] = 1
    elif occupation == "Retired" and "occupation_Retired" in df.columns:
        df.at[0, "occupation_Retired"] = 1

    if current_brand == "Newcomer" and "current_brand_Newcomer" in df.columns:
        df.at[0, "current_brand_Newcomer"] = 1

    if reasons == "Brand Reputation" and "reasons_for_choosing_brands_Brand Reputation" in df.columns:
        df.at[0, "reasons_for_choosing_brands_Brand Reputation"] = 1
    elif reasons == "Price" and "reasons_for_choosing_brands_Price" in df.columns:
        df.at[0, "reasons_for_choosing_brands_Price"] = 1
    elif reasons == "Quality" and "reasons_for_choosing_brands_Quality" in df.columns:
        df.at[0, "reasons_for_choosing_brands_Quality"] = 1

    if flavor == "Traditional" and "flavor_preference_Traditional" in df.columns:
        df.at[0, "flavor_preference_Traditional"] = 1

    if channel == "Retail Store" and "purchase_channel_Retail Store" in df.columns:
        df.at[0, "purchase_channel_Retail Store"] = 1

    if packaging == "Premium" and "packaging_preference_Premium" in df.columns:
        df.at[0, "packaging_preference_Premium"] = 1
    elif packaging == "Simple" and "packaging_preference_Simple" in df.columns:
        df.at[0, "packaging_preference_Simple"] = 1

    if situation == "Casual (eg. At home)" and \
       "typical_consumption_situations_Casual (eg. At home)" in df.columns:
        df.at[0, "typical_consumption_situations_Casual (eg. At home)"] = 1
    elif situation == "Social (eg. Parties)" and \
         "typical_consumption_situations_Social (eg. Parties)" in df.columns:
        df.at[0, "typical_consumption_situations_Social (eg. Parties)"] = 1

    return df

def predict(age, gender, zone, occupation, income_levels, consume_freq,
            current_brand, size, awareness, reasons, flavor, channel,
            packaging, health, situation):
    X = preprocess_input(age, gender, zone, occupation, income_levels, consume_freq,
                         current_brand, size, awareness, reasons, flavor, channel,
                         packaging, health, situation)
    y_pred = model.predict(X)
    y = y_pred[0] if hasattr(y_pred, "__len__") else y_pred
    return _decode_label(y)

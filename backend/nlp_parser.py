import re


def extract_parameters(user_text):

    text = user_text.lower()

    # ==================================
    # DEFAULT VALUES
    # ==================================

    params = {
        "hardness": 60,
        "density": 7.5,
        "temperature": 300,
        "load": 100,
        "speed": 500
    }

    # ==================================
    # APPLICATION BASED INFERENCE
    # ==================================

    if any(word in text for word in [
        "aerospace",
        "aircraft",
        "drone",
        "aviation"
    ]):
        params.update({
            "hardness": 80,
            "density": 4.5,
            "temperature": 500,
            "load": 120,
            "speed": 800
        })

    elif any(word in text for word in [
        "automobile",
        "car",
        "engine",
        "gear"
    ]):
        params.update({
            "hardness": 75,
            "density": 7.8,
            "temperature": 400,
            "load": 150,
            "speed": 700
        })

    elif any(word in text for word in [
        "bearing",
        "rotating",
        "shaft",
        "motor"
    ]):
        params.update({
            "hardness": 85,
            "density": 7.8,
            "temperature": 350,
            "load": 120,
            "speed": 900
        })

    # ==================================
    # HARDNESS
    # ==================================

    if any(word in text for word in [
        "hard",
        "wear resistant",
        "abrasion resistant",
        "scratch resistant"
    ]):
        params["hardness"] = 90

    elif any(word in text for word in [
        "soft",
        "flexible"
    ]):
        params["hardness"] = 20

    # ==================================
    # DENSITY
    # ==================================

    if any(word in text for word in [
        "lightweight",
        "light weight",
        "portable",
        "low weight"
    ]):
        params["density"] = 2.5

    elif any(word in text for word in [
        "heavy",
        "high density",
        "dense"
    ]):
        params["density"] = 9.0

    # ==================================
    # TEMPERATURE
    # ==================================

    if any(word in text for word in [
        "high temperature",
        "heat resistant",
        "thermal",
        "hot environment",
        "furnace"
    ]):
        params["temperature"] = 650

    elif any(word in text for word in [
        "low temperature",
        "cold environment",
        "cryogenic"
    ]):
        params["temperature"] = 50

    # ==================================
    # LOAD
    # ==================================

    if any(word in text for word in [
        "heavy load",
        "high load",
        "industrial",
        "high pressure"
    ]):
        params["load"] = 180

    elif any(word in text for word in [
        "light load",
        "small load"
    ]):
        params["load"] = 40

    # ==================================
    # SPEED
    # ==================================

    if any(word in text for word in [
        "high speed",
        "fast rotating",
        "high rpm",
        "turbine"
    ]):
        params["speed"] = 950

    elif any(word in text for word in [
        "low speed",
        "slow moving"
    ]):
        params["speed"] = 150

    # ==================================
    # LOW FRICTION APPLICATIONS
    # ==================================

    if any(word in text for word in [
        "low friction",
        "lubrication",
        "self lubricating"
    ]):
        params["hardness"] = 25
        params["density"] = 2.0

    # ==================================
    # EXPLICIT NUMBERS
    # ==================================

    temp_match = re.search(r'(\d+)\s*(c|°c)', text)
    if temp_match:
        params["temperature"] = float(
            temp_match.group(1)
        )

    rpm_match = re.search(r'(\d+)\s*rpm', text)
    if rpm_match:
        params["speed"] = float(
            rpm_match.group(1)
        )

    load_match = re.search(r'(\d+)\s*kg', text)
    if load_match:
        params["load"] = float(
            load_match.group(1)
        )

    hardness_match = re.search(r'(\d+)\s*hv', text)
    if hardness_match:
        params["hardness"] = float(
            hardness_match.group(1)
        )

    density_match = re.search(
        r'(\d+\.?\d*)\s*g/cm',
        text
    )

    if density_match:
        params["density"] = float(
            density_match.group(1)
        )

    return params
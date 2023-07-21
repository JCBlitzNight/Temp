def get_country_code(country_name):
    try:
        # Try the default format first
        country_code = pycountry_convert.country_name_to_country_alpha2(country_name, cn_name_format="default")
        return country_code
    except Exception:
        try:
            # If default format fails, try the fuzzy format
            country_code = pycountry_convert.country_name_to_country_alpha2(country_name, cn_name_format="fuzzy")
            return country_code
        except Exception:
            # If both formats fail, try the custom mappings
            return custom_country_mappings.get(country_name, None)

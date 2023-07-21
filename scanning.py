 try:
        # Try to find the ISO code using pycountry_convert
        country_code = pycountry_convert.country_name_to_country_alpha2(country_name, cn_name_format="default")
        continent_code = pycountry_convert.country_alpha2_to_continent_code(country_code)

        if country_code and continent_code:
            country_data.append({"id": country_code, "category": country_name, "value": count, "continent": continent_code})

    except Exception as e:
        print(f"Error processing country '{country_name}': {e}")

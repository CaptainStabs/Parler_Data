# Parler_Data
68k_Parler_Points.kmz is for Google Earth.

68k Parler Geotags.txt is the raw extraction.

# Scripts
I learned *after* writing all these scripts that someone else had already done it, and done it better. Mostly written just to cement my understanding of dictionaries.

geo2.py - Extracts coordinates from all the metadata

extract_vendor.py - Extracts device vendor and model from metadata and saves them in [brand,model] format in outfile.

count3.py - Takes data outputed by extract_vendor.py and formats it into a dictionary

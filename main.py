import os
from flask import Flask, request, render_template, jsonify, send_file
from phonenumbers import geocoder, carrier, timezone, parse
from opencage.geocoder import OpenCageGeocode
import folium
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()
key = os.getenv("api_key")

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process_phone_number():
    phone_number = request.form.get("phone_number")
    print(key)
    print(phone_number)
    app.logger.debug(f"Received data: {request.form}")

    phone_number = request.form.get("phone_number")
    if not phone_number:
        return jsonify({"error": "Phone number is required."}), 400
    
    try:
        # Parse and get details
        tPhoneNumber = parse(phone_number)
        country_name = geocoder.description_for_number(tPhoneNumber, "en")
        network_provider = carrier.name_for_number(tPhoneNumber, "en")
        time_zone = timezone.time_zones_for_number(tPhoneNumber)
        
        # Geolocation
        geocoder_service = OpenCageGeocode(key)
        location_obj = geocoder_service.geocode(country_name)
        lat = location_obj[0]['geometry']['lat']
        lng = location_obj[0]['geometry']['lng']
        location_details = geocoder_service.reverse_geocode(lat, lng)
        location = location_details[0]['formatted']

        # Generate Map
        target_map = folium.Map(location=[lat, lng], zoom_start=9)
        folium.Marker([lat, lng], popup=location).add_to(target_map)
        map_file_path = "static/location.html"
        target_map.save(map_file_path)

        # Response data
        response = {
            "network_provider": network_provider,
            "time_zone": list(time_zone),
            "location": location,
            "map_file": "/static/location.html",
        }
        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/download")
def download_map():
    map_file_path = "static/location.html"
    return send_file(map_file_path, as_attachment=True)

DEBUG_MODE = os.getenv('DEBUG_MODE') == "True"

if __name__ == "__main__":
    app.run(debug=DEBUG_MODE)

import json
import pickle
import implicit
from flask import Flask, jsonify, request
from helpers import parse_data, predict_user

app = Flask(__name__)

# load turicreate model
with open("x5_implicit.pkl", "rb") as f:
    (
        model,
        client_dict,
        reverse_client_dict,
        product_dict,
        reverse_product_dict,
    ) = pickle.load(f)
matrix_shape = (1, max(reverse_product_dict.keys()) + 1)
# baseline
baseline = {
    "recommended_products": [
        "4009f09b04",
        "15ccaa8685",
        "bf07df54e1",
        "3e038662c0",
        "4dcf79043e",
        "f4599ca21a",
        "5cb93c9bc5",
        "4a29330c8d",
        "439498bce2",
        "343e841aaa",
        "0a46068efc",
        "dc2001d036",
        "31dcf71bbd",
        "5645789fdf",
        "113e3ace79",
        "f098ee2a85",
        "53fc95e177",
        "080ace8748",
        "4c07cb5835",
        "ea27d5dc75",
        "cbe1cd3bb3",
        "1c257c1a1b",
        "f5e18af323",
        "5186e12ff4",
        "6d0f84a0ac",
        "f95785964a",
        "ad865591c6",
        "ac81544ebc",
        "de25bccdaf",
        "f43c12d228",
    ]
}


@app.route("/ready")
def ready():
    return "OK"


@app.route("/recommend", methods=["POST"])
def recommend():
    try:
        data = request.json
        user_id, user_frame = parse_data(data)
        products = user_frame["product_id"].to_list()
        if not products:
            return jsonify(baseline)
        else:
            # второй хак - добавим товаров из топа, если мало порекомендовали
            predictions = [
                pred
                for pred in predict_user(
                    model, products, product_dict, reverse_product_dict, matrix_shape,
                )
            ]
            predictions = predictions + [
                base_task
                for base_task in baseline["recommended_products"]
                if base_task not in predictions
            ]
            return jsonify({"recommended_products": predictions[:30]})
    except Exception as e:
        return jsonify(baseline)


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host="0.0.0.0", debug=True, port=8000)

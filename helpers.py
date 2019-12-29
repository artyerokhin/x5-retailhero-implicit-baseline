import pandas as pd
import numpy as np
import scipy


def parse_data(query_data):
    client = query_data.get("client_id", None)
    history = query_data.get("transaction_history", None)
    products = []

    if not client:
        return None, None

    if history:
        for session in history:
            session_products = session.get("products", None)
            if session_products:
                for product in session_products:
                    products.append([client, product["product_id"]])
        return client, pd.DataFrame(products, columns=["client_id", "product_id"])
    else:
        return None, None


def sort_by_dict(lst, dct):
    counts = []

    for element in lst:
        counts.append((element, dct.get(element, 0)))

    return [count[0] for count in sorted(counts, key=lambda x: x[1], reverse=True)]


def predict_user(model, user_id, products, product_dict, reverse_product_dict, matrix_shape):
    enum_clients = np.zeros(len(products))
    enum_products = np.array([product_dict[product] for product in products])

    sparse_matrix = scipy.sparse.csr_matrix((np.ones(shape=(len(enum_clients))),
                                             (enum_clients, enum_products)),
                                            shape=matrix_shape)

    rec = model.recommend(0, sparse_matrix, N=30, recalculate_user=True,
                          filter_already_liked_items=False)

    return [[user_id, reverse_product_dict[r[0]]] for r in rec]

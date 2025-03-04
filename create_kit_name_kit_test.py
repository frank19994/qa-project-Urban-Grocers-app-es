import data
import sender_stand_request

def get_token_user_new():
        response= sender_stand_request.post_new_client_kit(data.user_body)
        return response.json()["authToken"]

def get_name_kit(kit_body):
    name_current=data.kit_body.copy()
    name_current["name"]= kit_body
    return name_current

def positive_assert(kit_body):
    response= sender_stand_request.post_new_kit(kit_body,get_token_user_new())
    assert response.status_code == 201
    assert response.json()["name"]==kit_body["name"]


def negative_assert(kit_body):
    response= sender_stand_request.post_new_kit(kit_body,get_token_user_new())
    assert response.status_code == 400

def test_create_a_new_kit_with_1_letter_get_success_response():
        name_current = get_name_kit("a")
        positive_assert(name_current)

def test_create_a_new_kit_with_511_letter_get_success_response():
    name_current = get_name_kit("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    positive_assert(name_current)

def test_create_a_new_kit_empty_letter_get_error_response():
    name_current = get_name_kit("")
    negative_assert(name_current)

def test_create_a_new_kit_with_512_letter_get_success_response():
    name_current = get_name_kit("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabCa")
    negative_assert(name_current)

def test_create_a_new_kit_special_symbol_get_success_response():
    name_current=get_name_kit("\"№%@\",")
    positive_assert(name_current)

def test_create_a_new_kit_has_space_get_success_response():
    name_current=get_name_kit("aa a")
    positive_assert(name_current)

def test_create_a_new_kit_with_integer_string_get_success_response():
    name_current=get_name_kit("12345")
    positive_assert(name_current)

def test_create_kit_with_empty_body_get_error_response():
    name_current=get_name_kit()
    negative_assert(name_current)

def test_create_kit_with_numeric_type_name():
    name_current=get_name_kit(12345)
    negative_assert(name_current)

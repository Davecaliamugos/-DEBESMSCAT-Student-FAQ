from faq_data import FAQS
from utils import find_best_match


def get_response(user_input):
    response = find_best_match(user_input, FAQS)
 
    if response:
        return response
    else:
        return "I'm sorry, I don't have information about that. Please ask something related to DEBESMSCAT."
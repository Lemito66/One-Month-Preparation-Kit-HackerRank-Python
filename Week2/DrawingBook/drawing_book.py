def page_count(number_of_page_in_the_book, page_number_to_turn_to):
    page_in_the_book = []
    for page in range(1,number_of_page_in_the_book+1,2):
        page_in_the_book.append(page)
    if page_number_to_turn_to %2==0:
      new_page_to_search = page_number_to_turn_to +1
    else:
      new_page_to_search = page_number_to_turn_to
    page_in_the_book.index(new_page_to_search)
    result = (len(page_in_the_book)-page_in_the_book.index(new_page_to_search))-1
    return page_in_the_book, page_in_the_book.index(new_page_to_search), result
    
print(page_count(5, 2))
def page_count(number_of_page_in_the_book, page_number_to_turn_to):
    page_in_the_book = []
    results = []
    if number_of_page_in_the_book %2==0:
        number_of_page_in_the_book +=1
    for page in range(1,number_of_page_in_the_book+1,2):
        page_in_the_book.append(page)
    if page_number_to_turn_to %2==0:
      new_page_to_search = page_number_to_turn_to +1
    else:
      new_page_to_search = page_number_to_turn_to
      
    position_to_search = page_in_the_book.index(new_page_to_search)
    first_position = page_in_the_book.index(page_in_the_book[0])
    final_position = page_in_the_book.index(page_in_the_book[-1])
    first_result = position_to_search - first_position
    second_result = final_position - position_to_search
    results.append(first_result)
    results.append(second_result)
    return min(results)
    
print(page_count(6, 4))
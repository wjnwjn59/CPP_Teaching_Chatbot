## happy path
* greet
  - utter_greet
* feeling_good
  - utter_reply_feeling_good

## sad path 1
* greet
  - utter_greet
* feeling_bad
  - utter_reply_feeling_bad
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* feeling_bad
  - utter_reply_feeling_bad
  - utter_did_that_help
* deny
  - utter_sorry

## normal conversation 1
* greet
  - utter_greet
* health_inquire
  - utter_reply_health_inquire

## normal conversation 2
* greet
  - utter_greet
* health_inquire
  - utter_reply_health_inquire
* goodbye
  - utter_goodbye

## normal conversation 3
* greet
 - utter_greet
* goodbye
  - utter_goodbye

## say hello
* greet
  - utter_greet
  - utter_who_i_am

## say goodbye
* goodbye
  - utter_goodbye

## unknown asking 1
* want_to_ask
  - utter_accept_questions

## unknown asking 2
* greet
  - utter_greet
  - utter_who_i_am
* want_to_ask
  - utter_accept_questions
* stop_asking
  - utter_reply_stop_asking

## c++ what asking 1
* c++_what_asking{"c++_content":"c++"}
  - cpp_content_form
  - form{"name": "cpp_content_form"}
  - form{"name": null}
  - action_c++_content_answer
  - utter_ask_anything_else

## c++ what asking 2
* greet 
  - utter_greet
* want_to_ask
  - utter_accept_questions
* c++_what_asking{"c++_content":"c++"}
  - cpp_content_form
  - form{"name": "cpp_content_form"}
  - form{"name": null}
  - action_c++_content_answer
  - utter_ask_anything_else
* thanks
  - utter_reply_thanks

## c++ what asking 3
* want_to_ask
  - utter_accept_questions
* c++_what_asking{"c++_content":"c++"}
  - cpp_content_form
  - form{"name": "cpp_content_form"}
  - form{"name": null}
  - action_c++_content_answer
  - utter_ask_anything_else

## c++ what asking 4
* greet
  - utter_greet
* c++_what_asking{"c++_content":"c++"}
  - cpp_content_form
  - form{"name": "cpp_content_form"}
  - form{"name": null}
  - action_c++_content_answer
  - utter_ask_anything_else
* goodbye
  - utter_goodbye

## c++ what asking 5
* c++_what_asking{"c++_content":"c++"}
  - cpp_content_form
  - form{"name": "cpp_content_form"}
  - form{"name": null}
  - action_c++_content_answer
  - utter_ask_anything_else
* compliment
  - utter_reply_compliment

## c++ what asking 6
* c++_what_asking{"c++_content":"c++"}
  - cpp_content_form
  - form{"name": "cpp_content_form"}
  - form{"name": null}
  - action_c++_content_answer
  - utter_ask_anything_else
* stop_asking
  - utter_reply_stop_asking
  - utter_thanks

## c++ what asking 7
* c++_what_asking{"c++_content":"c++"}
  - cpp_content_form
  - form{"name": "cpp_content_form"}
  - form{"name": null}
  - action_c++_content_answer
  - utter_ask_anything_else
* continue_asking
  - utter_accept_questions
* c++_what_asking{"c++_content":"c++"}
  - cpp_content_form
  - form{"name": "cpp_content_form"}
  - form{"name": null}
  - action_c++_content_answer
  - utter_ask_anything_else

## c++ why asking 1
* c++_why_asking{"c++_content":"c++"}
  - cpp_content_form
  - form{"name": "cpp_content_form"}
  - form{"name": null}
  - action_c++_content_answer
  - utter_ask_anything_else


## c++ why asking 2
* greet 
  - utter_greet
* want_to_ask
  - utter_accept_questions
* c++_why_asking{"c++_content": "c++"}
  - cpp_content_form
  - form{"name": "cpp_content_form"}
  - form{"name": null}
  - action_c++_content_answer
  - utter_ask_anything_else
* thanks
  - utter_reply_thanks

## c++ why asking 3
* want_to_ask
  - utter_accept_questions
* c++_why_asking{"c++_content":"c++"}
  - cpp_content_form
  - form{"name": "cpp_content_form"}
  - form{"name": null}
  - action_c++_content_answer
  - utter_ask_anything_else

## c++ why asking 4
* greet
  - utter_greet
* c++_why_asking{"c++_content":"c++"}
  - cpp_content_form
  - form{"name": "cpp_content_form"}
  - form{"name": null}
  - action_c++_content_answer
  - utter_ask_anything_else
* goodbye
  - utter_goodbye

## c++ why asking 5
* c++_why_asking{"c++_content":"c++"}
  - cpp_content_form
  - form{"name": "cpp_content_form"}
  - form{"name": null}
  - action_c++_content_answer
  - utter_ask_anything_else
* compliment
  - utter_reply_compliment

## c++ why asking 6
* c++_why_asking{"c++_content":"c++"}
  - cpp_content_form
  - form{"name": "cpp_content_form"}
  - form{"name": null}
  - action_c++_content_answer
  - utter_ask_anything_else
* stop_asking
  - utter_reply_stop_asking
  - utter_thanks

## c++ why asking 7
* c++_why_asking{"c++_content":"c++"}
  - cpp_content_form
  - form{"name": "cpp_content_form"}
  - form{"name": null}
  - action_c++_content_answer
  - utter_ask_anything_else
* continue_asking
  - utter_accept_questions
* c++_why_asking{"c++_content":"c++"}
  - cpp_content_form
  - form{"name": "cpp_content_form"}
  - form{"name": null}
  - action_c++_content_answer
  - utter_ask_anything_else

## c++ how asking 1
* c++_how_asking{"c++_content":"c++"}
  - cpp_content_form
  - form{"name": "cpp_content_form"}
  - form{"name": null}
  - action_c++_content_answer
  - utter_ask_anything_else

## c++ how asking 2
* greet 
  - utter_greet
* want_to_ask
  - utter_accept_questions
* c++_how_asking{"c++_content":"c++"}
  - cpp_content_form
  - form{"name": "cpp_content_form"}
  - form{"name": null}
  - action_c++_content_answer
  - utter_ask_anything_else
* thanks
  - utter_reply_thanks

## c++ how asking 3
* want_to_ask
  - utter_accept_questions
* c++_how_asking{"c++_content":"c++"}
  - cpp_content_form
  - form{"name": "cpp_content_form"}
  - form{"name": null}
  - action_c++_content_answer
  - utter_ask_anything_else

## c++ how asking 4
* greet
  - utter_greet
* c++_how_asking{"c++_content":"c++"}
  - cpp_content_form
  - form{"name": "cpp_content_form"}
  - form{"name": null}
  - action_c++_content_answer
  - utter_ask_anything_else
* goodbye
  - utter_goodbye

## c++ how asking 5
* c++_how_asking{"c++_content":"c++"}
  - cpp_content_form
  - form{"name": "cpp_content_form"}
  - form{"name": null}
  - action_c++_content_answer
  - utter_ask_anything_else
* compliment
  - utter_reply_compliment

## c++ how asking 6
* c++_how_asking{"c++_content":"c++"}
  - cpp_content_form
  - form{"name": "cpp_content_form"}
  - form{"name": null}
  - action_c++_content_answer
  - utter_ask_anything_else
* stop_asking
  - utter_reply_stop_asking
  - utter_thanks

## c++ how asking 7
* c++_how_asking{"c++_content":"c++"}
  - cpp_content_form
  - form{"name": "cpp_content_form"}
  - form{"name": null}
  - action_c++_content_answer
  - utter_ask_anything_else
* continue_asking
  - utter_accept_questions
* c++_how_asking{"c++_content":"c++"}
  - cpp_content_form
  - form{"name": "cpp_content_form"}
  - form{"name": null}
  - action_c++_content_answer
  - utter_ask_anything_else

## c++ when asking 1
* c++_when_asking{"c++_content":"c++"}
  - cpp_content_form
  - form{"name": "cpp_content_form"}
  - form{"name": null}
  - action_c++_content_answer
  - utter_ask_anything_else

## c++ when asking 2
* greet 
  - utter_greet
* want_to_ask
  - utter_accept_questions
* c++_when_asking{"c++_content":"c++"}
  - cpp_content_form
  - form{"name": "cpp_content_form"}
  - form{"name": null}
  - action_c++_content_answer
  - utter_ask_anything_else
* thanks
  - utter_reply_thanks

## c++ when asking 3
* want_to_ask
  - utter_accept_questions
* c++_when_asking{"c++_content":"c++"}
  - cpp_content_form
  - form{"name": "cpp_content_form"}
  - form{"name": null}
  - action_c++_content_answer
  - utter_ask_anything_else

## c++ when asking 4
* greet
  - utter_greet
* c++_when_asking{"c++_content":"c++"}
  - cpp_content_form
  - form{"name": "cpp_content_form"}
  - form{"name": null}
  - action_c++_content_answer
  - utter_ask_anything_else
* goodbye
  - utter_goodbye

## c++ when asking 5
* c++_when_asking{"c++_content":"c++"}
  - cpp_content_form
  - form{"name": "cpp_content_form"}
  - form{"name": null}
  - action_c++_content_answer
  - utter_ask_anything_else
* compliment
  - utter_reply_compliment

## c++ when asking 6
* c++_when_asking{"c++_content":"c++"}
  - cpp_content_form
  - form{"name": "cpp_content_form"}
  - form{"name": null}
  - action_c++_content_answer
  - utter_ask_anything_else
* stop_asking
  - utter_reply_stop_asking
  - utter_thanks

## c++ when asking 7
* c++_when_asking{"c++_content":"c++"}
  - cpp_content_form
  - form{"name": "cpp_content_form"}
  - form{"name": null}
  - action_c++_content_answer
  - utter_ask_anything_else
* continue_asking
  - utter_accept_questions
* c++_when_asking{"c++_content":"c++"}
  - cpp_content_form
  - form{"name": "cpp_content_form"}
  - form{"name": null}
  - action_c++_content_answer
  - utter_ask_anything_else

## c++ where asking 1
* c++_where_asking{"c++_content":"c++"}
  - cpp_content_form
  - form{"name": "cpp_content_form"}
  - form{"name": null}
  - action_c++_content_answer
  - utter_ask_anything_else

## c++ where asking 2
* greet 
  - utter_greet
* want_to_ask
  - utter_accept_questions
* c++_where_asking{"c++_content":"c++"}
  - cpp_content_form
  - form{"name": "cpp_content_form"}
  - form{"name": null}
  - action_c++_content_answer
  - utter_ask_anything_else
* thanks
  - utter_reply_thanks

## c++ where asking 3
* want_to_ask
  - utter_accept_questions
* c++_where_asking{"c++_content":"c++"}
  - cpp_content_form
  - form{"name": "cpp_content_form"}
  - form{"name": null}
  - action_c++_content_answer
  - utter_ask_anything_else

## c++ where asking 4
* greet
  - utter_greet
* c++_where_asking{"c++_content":"c++"}
  - cpp_content_form
  - form{"name": "cpp_content_form"}
  - form{"name": null}
  - action_c++_content_answer
  - utter_ask_anything_else
* goodbye
  - utter_goodbye

## c++ where asking 5
* c++_where_asking{"c++_content":"c++"}
  - cpp_content_form
  - form{"name": "cpp_content_form"}
  - form{"name": null}
  - action_c++_content_answer
  - utter_ask_anything_else
* compliment
  - utter_reply_compliment

## c++ where asking 6
* c++_where_asking{"c++_content":"c++"}
  - cpp_content_form
  - form{"name": "cpp_content_form"}
  - form{"name": null}
  - action_c++_content_answer
  - utter_ask_anything_else
* stop_asking
  - utter_reply_stop_asking
  - utter_thanks

## c++ where asking 7
* c++_where_asking{"c++_content":"c++"}
  - cpp_content_form
  - form{"name": "cpp_content_form"}
  - form{"name": null}
  - action_c++_content_answer
  - utter_ask_anything_else
* continue_asking
  - utter_accept_questions
* c++_where_asking{"c++_content":"c++"}
  - cpp_content_form
  - form{"name": "cpp_content_form"}
  - form{"name": null}
  - action_c++_content_answer
  - utter_ask_anything_else

## anything else? - yes
- utter_ask_anything_else
* affirm
  - utter_accept_questions

## anything else? - no
- utter_ask_anything_else
* deny
  - utter_ok
  - utter_thanks

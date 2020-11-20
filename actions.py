from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction

class AnswerCppDefineQuestion(Action):

    def name(self) -> Text:
         return "action_c++_content_answer"

    def run(self, dispatcher: CollectingDispatcher,
         tracker: Tracker,
         domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
         cplusplus_content = tracker.get_slot("c++_content")
         
         all_answers_what = {
             'variable' : "Biến (Variable) trong C++ là là tên của một vùng trong bộ nhớ RAM, được sử dụng để lưu trữ thông tin. Bạn có thể gán thông tin cho một biến, và có thể lấy thông tin đó ra để sử dụng. Khi một biến được khai báo, một vùng trong bộ nhớ sẽ dành cho các biến.",
             'comment' : "Comment là một dòng hoặc nhiều dòng văn bản, được chèn vào source code chương trình, nhằm làm cho source code trở nên dễ hiểu hơn với người đọc, được bỏ qua bởi compiler và interpreter.",
             'cplusplus' : '''Ngôn ngữ C++ được Bjarne Stroustrup phát triển từ ngôn ngữ C từ cuối thập niên 1970.
             _ C++ là một phiên bản mở rộng của ngôn ngữ C, kết hợp tất cả các tính năng đã có của C.
             _ C++ được coi như là ngôn ngữ bậc trung (middle-level), kết hợp các đặc điểm và tính năng của ngôn ngữ bậc cao và bậc thấp.
             _ C++ có thể dùng để lập trình nhúng, lập trình hệ thống, hoặc những ứng dụng, game…
             _ C++ là ngôn ngữ "đa hướng". Nghĩa là nó hướng cấu trúc giống C và có thêm một tính năng cực kỳ quan trọng đó là tính năng hướng đối tượng. Các bạn sẽ được học phần hướng đối tượng của C++ trong serial Lập trình hướng đối tượng C++.
             _ C++ là một trong những ngôn ngữ lập trình phổ biết trên thế giới.
             '''
         }
         
         if cplusplus_content in all_answers_what:
            cplusplus_content_answer = all_answers_what[cplusplus_content]
         dispatcher.utter_message(text=cplusplus_content_answer)

         return [SlotSet("cplusplus_content_answer",cplusplus_content_answer)]

class CppContentForm(FormAction):
    def name(self) -> Text:
        """identifier của form """
        return 'cpp_content_form'

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """Danh sách các slots mà form cần phải có"""
        return ['c++_content']

    def slot_mapping(self) -> Dict[Text, Any]:
        return {'c++_content' : self.from_entity(entity='c++_content',
                                                  intent=['c++_what_asking', 'c++_why_asking', 'c++_how_asking',
                                                           'c++_when_asking', 'c++_where_asking'])
        }
    
    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any] 
               ) -> List[Dict]:
        """Sau khi đã có đủ các slots yêu cầu, sẽ pull câu trả lời từ db"""

        cplusplus_content = tracker.get_slot('c++_content')
        intent = tracker.latest_message['intent'].get('name')

        answer = ""

        if len(answer == 0):
            dispatcher.utter_message(
                "Xin lỗi bạn, mình hiện chưa thể trả lời được câu hỏi này >< Để mình ôn lại kiến thức tí nha :<"
            )
        return []

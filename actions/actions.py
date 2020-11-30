from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction
from rasa_sdk.types import DomainDict


class AnswerCppDefineQuestion(Action):

    def name(self) -> Text:
        return "action_c++_content_answer"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        cplusplus_content = tracker.get_slot("c++_content")

        curr_intent = tracker.latest_message['intent'].get('name')

        all_answers_what = {
            'comment': "Comment là một dòng hoặc nhiều dòng văn bản, được chèn vào source code chương trình, nhằm làm cho source code trở nên dễ hiểu hơn với người đọc, được bỏ qua bởi compiler và interpreter.",
            'cplusplus': '''Ngôn ngữ C++ được Bjarne Stroustrup phát triển từ ngôn ngữ C từ cuối thập niên 1970.
             _ C++ là một phiên bản mở rộng của ngôn ngữ C, kết hợp tất cả các tính năng đã có của C.
             _ C++ được coi như là ngôn ngữ bậc trung (middle-level), kết hợp các đặc điểm và tính năng của ngôn ngữ bậc cao và bậc thấp.
             _ C++ có thể dùng để lập trình nhúng, lập trình hệ thống, hoặc những ứng dụng, game…
             _ C++ là ngôn ngữ "đa hướng". Nghĩa là nó hướng cấu trúc giống C và có thêm một tính năng cực kỳ quan trọng đó là tính năng hướng đối tượng. Các bạn sẽ được học phần hướng đối tượng của C++ trong serial Lập trình hướng đối tượng C++.
             _ C++ là một trong những ngôn ngữ lập trình phổ biết trên thế giới.
             ''',
            'include': 'Include (Tạm dịch: Bao gồm) là một từ khóa trong C++ dùng để chỉ cho trình biên dịch biết rằng chúng ta cần sử dụng thư viện được khai báo và nó sẽ tự động thêm vào cho chúng ta. Cú pháp: #include <library_name>',
            'library': 'Library (Tạm dịch: Thư viện) là một tập mã nguồn đã được đóng gói, có thể được tái sử dụng trong nhiều chương trình khác nhau.',
            'namespace': 'Namespace (Tạm dịch: Không gian tên) là một từ khóa trong C++ được sử dụng để định nghĩa một phạm vi nhằm mục đích phân biệt các hàm, lớp, biến, ... cùng tên trong các thư viện khác nhau.',
            'pseudo code': 'Pseudo code (Tạm dịch: Mã giả) là một bản mô tả giải thuật lập trình máy tính ngắn gọn và không chính thức cấp cao, trong đó sử dụng những quy ước có cấu trúc của một số ngôn ngữ lập trình, nhưng thường bỏ đi những chi tiết không cần thiết để giúp hiểu rõ giải thuật hơn.',
            # Câu trả lời về các kiểu dữ liệu và biến
            'variable': "Variable (Tạm dịch: Biến) trong C++ là là tên của một vùng trong bộ nhớ RAM, được sử dụng để lưu trữ thông tin. Bạn có thể gán thông tin cho một biến, và có thể lấy thông tin đó ra để sử dụng. Khi một biến được khai báo, một vùng trong bộ nhớ sẽ dành cho các biến.",
            'unsigned': '''Unsigned (Tạm dịch: Không dấu) trong C++ là một kiểu dữ liệu số nguyên không dấu, chỉ cho phép ta chứa các số nguyên không âm. Điểm khác biệt giữa unsigned và int đó là miền giá trị của chúng!
              Việc khai báo unsigned <var_name> cũng sẽ tương tự như việc khai báo unsigned int <var_name>''',
            'signed': '''Signed (Tạm dịch: Có dấu) trong C++ là một kiểu dữ liệu số nguyên có dấu, cho phép ta chứa các giá trị âm hoặc dương!\n
             Việc khai báo signed <var_name> cũng sẽ tương tự như việc khai báo int <var_name>, signed int <var_name>.''',
            'short': '''Short (Tạm dịch: Ngắn) trong C++ là một kiểu dữ liệu số nguyên cho phép ta lưu trữ các số -2,-1,0,1,2,... tương tự với kiểu int. Điểm khác biệt của short so với int nằm ở việc có miền giá trị nhỏ hơn!''',
            'long': 'Long (Tạm dịch: Dài) trong C++ là một kiểu dữ liệu số nguyên cho phép ta lưu trữ các giá trị -2,-1,0,1,2,... tương tự với kiểu int. Điểm khác biệt của long so với int nằm ở việc có miền giá trị to hơn!',
            'type modififer': 'Type modifiers hay Modifers (Tạm dịch: Công cụ chỉnh sửa kiểu dữ liệu) trong C++ là các từ khóa đứng trước các kiểu dữ liệu cơ bản, làm thay đổi các tính chất mặc định của chúng như miền giá trị,... Trong C++ gồm có 4 modifers đó là: unsigned, signed, short và long.',
            'typedef': 'Typedef (Tạm dịch: Định nghĩa kiểu dữ liệu) trong C++ là một từ khóa cho phép ta định nghĩa thêm tên mới cho các kiểu dữ liệu có sẵn\nCú pháp như sau: typedef <data_type> <new_name>',
            'constant': 'Constant hay const (Tạm dịch: Hằng số) trong C++ là một từ khóa dùng để chỉ định một biến hay một đối tượng (trong OOP) là một hằng - tức không thể làm thay đổi giá trị của nó kể từ sau khi khai báo từ khóa const.',
            'macro': 'Macro trong C++ là một trong các chỉ thị trong bộ tiền xử lý (Preprocessing), dùng để đặt lại tên của một chức năng, khối lệnh, giá trị,... theo ý của mình.\nCú pháp: #define <new_name> <a syntax, code block,...>\n Mình cũng có ví dụ như sau, giả sử mình muốn định nghĩa giá trị 3.14 có tên gọi là PI, mình có thể sử dụng macro như sau: #define PI 3.14',
            'wchar_t': 'wchar_t trong C++ là một kiểu dữ liệu wide character. Wide character khá giống với kiểu char ngoại trừ việc nó chiếm gấp đôi bộ nhớ và có thể một giá trị lớn hơn kiểu char (> 256)',
            'boolean': 'Boolean hay bool (Tạm dịch: Kiểu luận lý) trong C++ là một kiểu dữ liệu đại số luận lý chỉ gồm có hai giá trị là 0 (false) và 1 (true).',
            'data type': 'Data type (Tạm dịch: Kiểu dữ liệu) trong C++ là một hệ thống dùng để phân biệt sự khác nhau về lượng tài nguyên chiếm trong bộ nhớ và cách diễn giải mẫu bit của các biến hoặc các hàm.',
            'array': 'Array (Tạm dịch: Mảng) trong C++ là một kiểu dữ liệu, gồm một tập hợp các phần tử có cùng kiểu dữ liệu với nhau, được phân biệt bởi số thứ tự (index) bên trong mảng, bắt đầu từ vị trí 0.\nCú pháp: <data_type> <variable_name>[<size_of_array>];',
            'structure': 'Structure hay struct (Tạm dịch: Cấu trúc) trong C++ là một cú pháp dùng để biểu diễn một kiểu dữ liệu mới dựa vào việc tập hợp các biến cần thiết với nhau.\nCú pháp: struct <name>{\n//some variables;\n};',
            'class': 'Class (Tạm dịch: Lớp) trong C++ là một kiến thức liên quan đến Lập trình hướng đối tượng (Object Oriented Programming), là một bản thiết kế của các đối tượng có cùng chung các đặc điểm, tính chất, hành vi... Trong lập trình, một class có thể chứa các Biến - Thuộc tính (Attributes) và các Hàm - Phương thức (Methods).\nCú pháp: class <class_name>{\n//Some attributes\n//Some methods\n};\nĐể có thể hiểu rõ hơn về Class, bạn hãy tìm hiểu thêm về Lập trình hướng đối tượng nhé!',
            'union': 'Union (Tạm dịch: Hợp nhất) trong C++ là một cú pháp về cơ bản giống với struct, dùng để gom nhóm các biến lại với nhau để từ đó hình thành một kiểu dữ liệu mới.\nCú pháp: union <union_name>{\n//some variables\n};',
            'pointer': 'Pointer (Tạm dịch: Con trỏ) trong C++ là một biến chứa địa chỉ của một biến khác với cùng kiểu dữ liệu đã được khai báo.\nCú pháp: <data_type>* <variable_name>;',
            'enumeration': 'Enumeration hay enum (Tạm dịch: Kiểu liệt kê) là một kiểu dữ liệu trong C++ dùng để định nghĩa một tập các hằng số cố định,',
            'integer': 'Integer hay int (Tạm dịch: Kiểu số nguyên) trong C++ là một kiểu dữ liệu cho phép lưu trữ những giá trị là số nguyên như -2,-1,0,1,...\nCú pháp: int <variable_name>;',
            'floating_point': 'Floating point hay float (Tạm dịch: Kiểu dấu chấm động/kiểu số thực) trong C++ là một kiểu dữ liệu cho phép lưu trữ các số có dạng -1.1234, 5.5467, 3.14,... Nói cách khác, kiểu dấu chấm động cho phép ta lưu trữ cả phần thập phân của một số.\nCú pháp: float <variable_name>;',
            'double': 'Double trong C++ là một kiểu dữ liệu ctrong C++ là một kiểu dữ liệu cho phép lưu trữ các số có dạng -1.1234, 5.5467, 3.14,... giống như kiểu float. Điểm khác biệt của double so với float nằm ở việc có miền giá trị lớn hơn.\nCú pháp: double <variable_name>;',
            'character': 'Character hay char (Tạm dịch: Kiểu kí tự) trong C++ là một kiểu dữ liệu dùng để lưu trữ một ký tự trong bảng mã ASCII như 1,2,3,a,b,c,d,... Kiểu char còn đặc biệt ở chỗ, nó vừa là kiểu kí tự nhưng cũng vừa là kiểu số nguyên (integer), chính vì thế ta cũng thể sử dụng số để đại diện cho các kí tự theo bảng mã ASCII khi làm việc với kiểu char.\nCú pháp: char <variable_name>;',
            'string': 'String (Tạm dịch: Kiểu chuỗi kí tự) trong C++ là một kiểu dữ liệu tập hợp các kí tự được đặt trong dấu ngoặc kép, dùng để biểu diễn một đoạn văn bản,... Lưu ý rằng kiểu string không phải là một kiểu dữ liệu được dựng sẵn trong C++ mà nó được cài đặt trong thư viện STL, vì vậy để sử dụng được string trước tiên các bạn cần phải khai báo: #include <string> cái đã nha!\nCú pháp: std::string <variable_name>;',
            'local variable': 'Local variables (Tạm dịch: Biến cục bộ) trong C++ là một biến được định nghĩa bên trong một khối lệnh. ',
            'global variable': 'Global variables (Tạm dịch: Biến toàn cục) trong C++ rheo quy ước được khai báo ở đầu của một tập tin, bên dưới #include. Chính vì được khai báo ngay đầu tập tin mà không nằm trong phạm vi của một khối lệnh nào nên biến toàn cục - đúng với tên gọi của nó sẽ có phạm vi hoạt động là toàn bộ tập tin code, tức là ta có thể sử dụng nó ở bất kì đâu mà ta muốn.',
            'auto': 'Auto (Tạm dịch: Tự động) trong C++ 11 là một kiểu dữ liệu cho phép nhận diện kiểu dữ liệu của một biến thông qua giá trị ta khởi tạo nó, ví dụ nếu ta khai báo: auto aStr = 10; thì kiểu dữ liệu của aStr lúc này sẽ là kiểu int',
            'external': 'External Variables (Tạm dịch: Biến ngoại) là biến mà có thể dùng chung ở các sourcefile khác nhau. Để có thể khai báo external variables, ta cần phải sử dụng từ khóa extern khi khai báo biến, và việc khai báo các external variables nên được thực hiện ở các header file (file .h) để tiện sử dụng.',
            'static': 'Static (Tạm dịch: Tĩnh) trong C++ là một từ khóa có thể sử dụng để khai báo chung với biến, hàm hoặc các thuộc tính, phương thức trong một class (OOP). Với biến static, dù đặt bên trong hay bên ngoài khối lệnh thì nó vẫn sẽ có hiệu lực - tức bất kì sự thay đổi giá trị ở đâu cũng làm biến static cập nhật đúng với giá trị đó - giống với Biến toàn cục (Global variable).',
            'vector': 'Vector trong C++ là một đối tượng có thể chứa một chuỗi các vùng nhớ liên tiếp nằm trong thư viện STL, đại diện cho kiểu Mảng (Array) thông thường.\nKhá giống với kiểu Mảng về chức năng, nhưng bên cạnh đó Vector còn cho thấy thêm một số điểm ưu việt hơn so với Array như việc không cần phải khai báo kích thước vì Vector có thể tự động tăng kích thước của nó lên, có thể biết được số lượng phần tử đang lưu bên trong nó hay có thể dùng được số phần tử âm,...',
            'reference variable': 'Reference variables (Tạm dịch: Biến tham chiếu) là một biến có các đặc điểm sau đây:\n_Biến tham chiếu không được cấp phát bộ nhớ, không có địa chỉ riêng.\n_Nó dùng làm bí danh cho một biến (kiểu giá trị) nào đó và nó sử dụng vùng nhớ của biến này.\nCú pháp: <data_type> &<variable_name> = <any_declared_variable>;',
            # Câu trả lời về các toán tử
            'decrement operator': '''Decrement operators (Tạm dịch: Toán tử giảm, Ký hiệu: --) là loại toán tử giảm giá trị của biến xuống 1 đơn vị, có thể đứng trước hoặc sau một biến và ở mỗi vị trí khác nhau sẽ có một số điểm khác biệt:\n
             _ Prefix decrement (Đứng trước biến): giảm giá trị của biến lên trước rồi cập nhật giá trị mới vào biến ngay lập tức.\n
             _ Postfix decrement (Đứng sau biến): sử dụng giá trị cũ của biến tại thời điểm dòng code đang thực thi cho đến khi tới dòng code tiếp theo thì mới cập nhật giá trị mới của biến (tức đã giảm 1)''',
            'increment operator': '''Increment operators (Tạm dịch: Toán tử tăng, Ký hiệu: ++) là loại toán tử tăng giá trị của biến lên 1 đơn vị, có thể đứng trước hoặc sau một biến và ở mỗi vị trí khác nhau sẽ có một số điểm khác biệt:\n
             _ Prefix increment (Đứng trước biến): tăng giá trị của biến lên trước rồi cập nhật giá trị mới vào x ngay lập tức.\n
             _ Postfix increment (Đứng sau biến): sử dụng giá trị cũ của biến tại thời điểm dòng code đang thực thi cho đến khi tới dòng code tiếp theo thì mới cập nhật giá trị mới của biến (tức đã tăng 1)''',
            'deference operator': '''Dereference operators (Tạm dịch: Toán tử trỏ, Ký hiệu: *) là loại toán tử cho phép chúng ta truy cập vào giá trị tại một địa chỉ cụ thể.''',
            'address_of operator': '''Address_of operators (Tạm dịch: Toán tử địa chỉ, Ký hiệu : &) là loại toán tử cho phép chúng ta lấy địa chỉ bộ nhớ của một biến.''',
            'comma operator': '''Comma operator (Tạm dịch: Toán tử phẩy, Ký hiệu : ,) là một loại toán tử cho phép ta kết nối các biểu thức lại với nhau, thực thi theo trình tự từ trái sang phải. Giả sử ta có đoạn code sau:\n
             int a = 0;\n
             int b = (a + 100, a++, a + 100);\n
             cout << b << endl ; // Kết quả là 201\n''',
            'ternary operator': 'Ternary operators (Tạm dịch: Toán tử ba ngôi, Ký hiệu: ? :) là toán tử có 3 toán hạng trong biểu thức. Cú pháp: (<condition_expression>) ? <value_if_true> : <value_if_false);\nTrong đó:\n_condition_expression: là một biểu thức điều kiện kiểu bool, thứ sẽ quyết định kết quả của phép toán.\n_value_if_true: Nếu biểu thức điều kiện trả về true, đây là sẽ là kết quả của phép toán.\n_value_if_false: Nếu biểu thức điều kiện trả về false, đây là sẽ kết quả của phép toán.',
            'binary operator': 'Binary operators (Tạm dịch: Toán tử hai ngôi) là toán tử có 2 toán hạng trong biểu thức. Có 5 toán tử số học 2 ngôi trong C++ đó là: Cộng (Addition : +), Trừ (Subtraction : -), Nhân (Multiplication : *), Chia lấy nguyên (Division : /), Chia lấy dư (Modulus : %)',
            'unary operator': 'Unary operators (Tạm dịch: Toán tử một ngôi) là toán tử chỉ có 1 toán hạng trong biểu thức. Ví dụ như việc bạn sử dụng dấu - để biểu diễn số âm kiểu -11, -60,...',
            'shift operator': 'Shift operators (Tạm dịch: Toán tử dời bit) bao gồm toán tử dời qua phải (right-shift - >>) và toán tử dời qua trái (left-shift - <<).',
            'bitwise operator': '''Bitwise operators (Tạm dịch: Toán tử bit) là toán tử họa động trên các bits và thực hiện các phép toán liên quan đến bit như &(AND), |(OR), ^(XOR), ~(One's complement), <<(Left shift), >>(Right shift).''',
            'logical operator': 'Logical operators (Tạm dịch: Toán tử logic) là loại toán tử dùng để kết hợp hai hay nhiều điều kiện lại với nhau để đánh giá và đưa ra kết quả cuối cùng. Ta có toán tử AND (&& - chỉ đúng khi tất cả điều kiện đều đúng), toán tử OR (|| - chỉ đúng khi một trong các điều kiện là đúng) và toán tử NOT(! - chỉ đúng khi kết quả cuối cùng của biểu thức là sai)',
            'comparison operator': 'Comparison operators hay Relational operators (Tạm dịch: Toán tử so sánh) là loại toán tử cho phép thực hiện các phép toán so sánh như so sánh hơn, so sánh bằng,...',
            'arithmetic operator': 'Arithmetic operators (Tạm dịch: Toán tử số học) là loại toán tử dùng để biểu diễn các phép toán số học như +,-,*,/,%...',
            'assignment operator': 'Assignment Operators (Tạm dịch: Toán tử gán, Ký hiệu: =) là một loại toán tử dùng để cấp phát giá trị',
            'operator': 'Operators (Tạm dịch: Toán tử) trong lập trình là một biểu tượng đại diện cho các phép toán số học như cộng trừ nhân chia hay các phép toán logic,... và trả về một kết quả. Trong C++, có rất nhiều loại toán tử nhưng cơ bản và chung nhất, ta có thể chia toán tử làm ba loại: Toán tử một ngôi (Unary Operator), Toán tử hai ngôi (Binary Operator) và Toán tử ba ngôi (Ternary Operator).',
            # Câu trả lời về control flow
            'if': 'If hay If statements (Tạm dịch: Lệnh if) là một lệnh được dùng để kiểm tra một biểu thức kiểu luận lý nào đó là đúng hay sai, nếu đúng thì sẽ thực thi tập chỉ thị bên trong khối if, nếu điều kiện sai thì sẽ bỏ qua khối lệnh if đó.\n Cú pháp: if(<boolean_expression>){\n//some codes here...\n}\nChi tiết hơn, Lệnh if còn được phân loại thành 4 loại: if, if else, if else if Ladder và nested if',
            'loop': 'Loop (Tạm dịch: Sự lặp) trong lập trình là một khái niệm dùng để chỉ sự lặp đi lặp lại một tập các chỉ thị (một khối lệnh) cho đến khi thỏa mãn điều kiện để dừng vòng lặp cho trước. Trong C++, một vòng lặp được đại diện bởi các từ khóa for (for loop), while (while loop) và do while(do while loop).',
            'control flow': 'Control flow hay Flow of control (Tạm dịch: Cấu trúc điều khiển) trong lập trình là một khái niệm dùng để chỉ một tập các chỉ thị, các lệnh hay các lời gọi hàm được thực thi khi chạy chương trình.',
            'selection statement': 'Selection statements (Tạm dịch: Lệnh lựa chọn) trong lập trình là một khái niệm dùng để chỉ sự quyết định thực thi một tập các chỉ thị hay một khối lệnh dựa dựa trên một điều kiện cho trước. Trong C++, ta có thể dùng lệnh if hoặc lệnh switch để có thể sử dụng lệnh lựa chọn.',
            'iteration statement': 'Iteration statements hay Loop (Tạm dịch: Lệnh lặp) trong lập trình là một khái niệm dùng để chỉ sự lặp đi lặp lại một tập các chỉ thị (một khối lệnh) cho đến khi thỏa mãn điều kiện để dừng vòng lặp cho trước. Trong C++, một vòng lặp được đại diện bởi các từ khóa for (for loop), while (while loop) và do while(do while loop)',
            'jump statement': 'Jump statements (Tạm dịch: Lệnh nhảy) trong lập trình là một khái niệm dùng để chỉ sự làm thay đổi đột ngột hướng thực thi code một cách vô điều kiện sang một tập chỉ khác ở một nơi nào đó trong tập tin code của chúng ta. Trong C++, ta có thể biểu diễn Lệnh nhảy bằng các lệnh gồm Lệnh break, Lệnh continue, Lệnh goto và Lệnh return.',
            'for': '''For hay For loops (Tạm dịch: Vòng lặp for) trong C++ là một cấu trúc vòng lặp với chức năng tương tự như vòng while nhưng khác về cú pháp. Cấu trúc của một vòng for như sau:\nfor(<loop_variable_declaration>;<stop_condition_expression>;<update_loop_variable_expression>){\n//Some codes here...\n
             }\nVới:\n
             _ loop_variable_declation: là nơi khởi tạo biến lặp, biến lặp được sử dụng như là một máy đếm số lần đã lặp của vòng for.\n
             _ stop_condition_expression: là nơi khởi tạo một biểu thức kiểu bool cho biến lặp, khi không còn thỏa mãn biểu thức này (false) thì vòng lặp sẽ kết thúc.\n
             _ update_loop_variable_expression: là nơi khởi tạo một biểu thức để cập nhật giá trị cho biến lặp sau mỗi lần lặp.''',
            'while': 'While hay While loops (Tạm dịch: Vòng lặp while) trong C++ là một vòng lặp với chức năng tương tự như vòng for nhưng khác về cú pháp. Cấu trúc của một vòng while như sau:\nwhile(<condition_expression>){\n//some codes here...\n}\nMình thể hiểu đơn giản cấu trúc đó như sau: trong khi điều kiện <condition_expression> vẫn trả về kết quả đúng (true), thì các đoạn code bên trong dấu { } vẫn sẽ được thực thi.',
            'do while': '''do while (Tạm dịch: Vòng lặp do while) trong C++ là một vòng lặp khá giống với vòng lặp while, điểm khác biệt ở do while so với while là nó sẽ đảm bảo vòng lặp sẽ được lặp ít nhất một lần.Cú pháp:\n
             do {\n
                // Some codes here;\n
            } while (<condition_expression>);''',
            'switch': '''Switch statements (Tạm dịch: Lệnh chuyển mạch) trong C++ giống như là một chuỗi các câu lệnh if else với việc so sánh một biến với các số nguyên. Cú pháp:\n
             switch (n)\n
            {\n
                case 1: // Sẽ thực thi khối lệnh ở đây nếu n == 1;\n
                        break;\n
                case 2: // Sẽ thực thi khối lệnh ở đây nếu n == 2;\n
                        break;\n
                default: // Nếu n không bằng với bất kì case nào thì sẽ thực thi khối lệnh ở đây;
            }''',
            'break': 'Break statements (Tạm dịch: Lệnh chấm dứt) trong C++ là một trong các lệnh nhảy, dùng để kết thúc một vòng lặp ngay lập tức kể cả khi nó vẫn còn có thể tiếp tục lặp.',
            'continue': 'Continue statements (Tạm dịch: Lệnh tiếp tục) trong C++ là một trong các lệnh nhảy, dùng để ép buộc trình biên dịch phải nhảy đến lần lặp kế tiếp của một vòng lặp.',
            'goto': '''Goto statements (Tạm dịch: Lệnh goto) trong C++ là một trong các lệnh nhảy, dùng để thực hiện việc đẩy trình biên dịch đến một đoạn code khác (label) và thực thi chúng. Cú pháp:\n
             // some code heres...;\n
             goto <label_name>;\n
            
             <label_name>:\n
             // some codes here;''',
            'if else': '''if else (Tạm dịch: Nếu không thì...) là một dạng đặc biệt của lệnh if khi mà ta có thể định nghĩa thêm một khối lệnh cho trường hợp biểu thức điều kiện sai.Ví dụ như sau:\n
             if(a == 1){\n
                // Some codes here;\n
             }\n
             else { // Nếu a != 1 thì sẽ thực thi đoạn code ở đây\n
                // Some code here;\n
             }''',
            'if else if ladder': '''if else if Ladder (Tạm dịch: Cầu thang if else) là một dạng đặc biệt của lệnh if khi ta định nghĩa thêm nhiều lệnh if hơn sau mỗi else. Ví dụ như sau:\n
             if(a == 1){\n
                // Some code heres;\n
             }\n
             else if (a == 2){\n
                // Some code heres;\n
             }\n
             else if (a == 3){\n
                // Some code heres;\n
             }''',
            'nested if': '''Nested if (Tạm dịch: if lồng if) là một dạng đặc biệt của lệnh if khi bên trong khối lệnh if lại có thêm một khối if khác nữa.Ví dụ như sau:\n
             if(a == 1){\n
                if(b == 2){ // Thêm một khối if nữa\n 
                    //Some codes here\n
                }\n
             }''',
            # Câu trả lời về function
            'function': 'Function (Tạm dịch: Hàm) là một đoạn các câu lệnh có thể tái sử dụng. Function cho phép lập trình viên cấu trúc chương trình thành những phân đoạn khác nhau để thực hiện những công việc khác nhau.',
            'parameter': 'Parameters (Tạm dịch: Tham số) là những gì chúng ta gọi khi định nghĩa một hàm. Parameter sẽ đại diện cho một giá trị mà hàm của bạn sẽ nhận được khi được gọi.',
            'argument': 'Arguments (Tạm dịch: Đối số) là đại diện cho giá trị truyền cho parameter khi chúng ta thực hiện lời gọi hàm. Mỗi argument sẽ tương ứng với một parameter khi khai báo.',
            'recursion': 'Recursion (Tạm dịch: Đệ quy) là một hàm tự gọi lại chính nó.',
            'pass by value': 'Pass by value (Tạm dich: Truyền tham trị) có thể được hiểu là giá trị của biến sẽ không bị thay đổi khi ta truyền biến này vào một hàm mà trong lúc thực thi đoạn code bên trong hàm có làm thay đổi giá trị của biến.',
            'pass by reference': 'Pass by reference (Tạm dịch: Truyền tham chiếu) có thể được hiểu là giá trị của biến sẽ bị thay đổi khi ta truyền biến này vào một hàm trong lúc thực thi đoạn code bên trong hàm có làm thay đổi giá trị của biến.',
            'return': 'Return keyword (Tạm dịch: Trả về) trong C++ là một từ khóa dùng để trả về một giá trị cho nơi gọi hàm, đây từ khóa bắt buộc đối với bất kì hàm nào được khai báo có giá trị trả về, và có thể có hoặc không đối với hàm khai báo kiểu void.',
            'return type': 'Return type (Tạm dịch: Kiểu trả về của hàm) trong C++ là việc định nghĩa kiểu giá trị mà hàm đó sẽ trả về cho nơi gọi hàm, giả sử ta khai báo một hàm kiểu int thì khi thực hiện lời gọi hàm, hàm này chắc chắn sẽ trả về một giá trị int.',
            'const reference': 'Const reference (Tạm dịch: Tham chiếu hằng) trong C++ là việc ta định nghĩa tham số truyền vào là tham chiếu với từ khóa const - tức là sẽ không thể thay đổi được giá trị của biến truyền vào hàm mặc dù đó là tham chiếu. Hiệu quả của việc sử dụng tham chiếu hằng chỉ thể hiện rõ khi làm việc với các đối tượng struct/class.',
            'inline function': 'Inline functions (Tạm dịch: Hàm nội tuyến) là một loại hàm trong ngôn ngữ lập trình C++. Từ khoá inline được sử dụng để đề nghị (không phải là bắt buộc) compiler (trình biên dịch) thực hiện inline expansion (khai triển nội tuyến) với hàm đó hay nói cách khác là chèn code của hàm đó tại địa chỉ mà nó được gọi.',
            'default value': 'Default values (Tạm dịch: Tham số mặc nhiên) là khi ta mặc định gán sẵn giá trị bất kì cho một tham số truyền vào khi thực hiện khai báo hàm. Điều đó đồng nghĩa, khi thực hiện lời gọi hàm mà không truyền vào đối số tương ứng, trình biên dịch sẽ sử dụng giá trị đã được gán sẵn cho tham số đó khi thực thi hàm.',
            'main function': 'Main function (Tạm dịch: Hàm main) trong C++ là một trường hợp của hàm, đây là nơi sẽ được thực thi đầu tiên khi chạy một chương trình C++.',
            'built in function': 'Built in functions (Tạm dịch: Hàm dựng sẵn) hay còn có tên gọi khác là Library functions, là các hàm ta có thể gọi nó trực tiếp mà không cần phải khai báo và định nghĩa chúng bởi vì chúng đã được viết sẵn trong các thư viện của C++ như thư viện stdio.h, iostream,...'
        }

        # Dict for answer why
        all_answers_why = {
            'comment': "Trong bất cứ ngành nghề nào, chắc chắn bạn không chỉ làm việc một mình, đặc biệt trong lập trình, bạn muốn đồng nghiệp hoặc những thế hệ sau có thể dễ dàng hiểu được và kế thừa những dòng code của bạn viết ra,\n hoặc để vài năm sau đọc lại bạn vẫn đảm bảo hiểu được mình viết gì trong đó.\n Để làm được chuyện đó, ngoài việc tuân thủ các coding convention, naming convention, ... thì một trong những cách truyền đạt ý nghĩa đoạn code của bạn cho mọi người \n đó chính là COMMENT.",
            'cplusplus': '''
            `
             ''',
            'include': 'Include (Tạm dịch: Bao gồm) là một từ khóa trong C++ dùng để chỉ cho trình biên dịch biết rằng chúng ta cần sử dụng thư viện được khai báo và nó sẽ tự động thêm vào cho chúng ta. Cú pháp: #include <library_name>',
            'library': 'Library (Tạm dịch: Thư viện) là một tập mã nguồn đã được đóng gói, có thể được tái sử dụng trong nhiều chương trình khác nhau.',
            'namespace': 'Namespace (Tạm dịch: Không gian tên) là một từ khóa trong C++ được sử dụng để định nghĩa một phạm vi nhằm mục đích phân biệt các hàm, lớp, biến, ... cùng tên trong các thư viện khác nhau.',
            'pseudo code': 'Pseudo code (Tạm dịch: Mã giả) là một bản mô tả giải thuật lập trình máy tính ngắn gọn và không chính thức cấp cao, trong đó sử dụng những quy ước có cấu trúc của một số ngôn ngữ lập trình, nhưng thường bỏ đi những chi tiết không cần thiết để giúp hiểu rõ giải thuật hơn.',
            # Câu trả lời về các kiểu dữ liệu và biến
            'variable': "Variable (Tạm dịch: Biến) trong C++ là là tên của một vùng trong bộ nhớ RAM, được sử dụng để lưu trữ thông tin. Bạn có thể gán thông tin cho một biến, và có thể lấy thông tin đó ra để sử dụng. Khi một biến được khai báo, một vùng trong bộ nhớ sẽ dành cho các biến.",
            'unsigned': '''Unsigned (Tạm dịch: Không dấu) trong C++ là một kiểu dữ liệu số nguyên không dấu, chỉ cho phép ta chứa các số nguyên không âm. Điểm khác biệt giữa unsigned và int đó là miền giá trị của chúng!
              Việc khai báo unsigned <var_name> cũng sẽ tương tự như việc khai báo unsigned int <var_name>''',
            'signed': '''Signed (Tạm dịch: Có dấu) trong C++ là một kiểu dữ liệu số nguyên có dấu, cho phép ta chứa các giá trị âm hoặc dương!\n
             Việc khai báo signed <var_name> cũng sẽ tương tự như việc khai báo int <var_name>, signed int <var_name>.''',
            'short': '''Short (Tạm dịch: Ngắn) trong C++ là một kiểu dữ liệu số nguyên cho phép ta lưu trữ các số -2,-1,0,1,2,... tương tự với kiểu int. Điểm khác biệt của short so với int nằm ở việc có miền giá trị nhỏ hơn!''',
            'long': 'Long (Tạm dịch: Dài) trong C++ là một kiểu dữ liệu số nguyên cho phép ta lưu trữ các giá trị -2,-1,0,1,2,... tương tự với kiểu int. Điểm khác biệt của long so với int nằm ở việc có miền giá trị to hơn!',
            'type modififer': 'Type modifiers hay Modifers (Tạm dịch: Công cụ chỉnh sửa kiểu dữ liệu) trong C++ là các từ khóa đứng trước các kiểu dữ liệu cơ bản, làm thay đổi các tính chất mặc định của chúng như miền giá trị,... Trong C++ gồm có 4 modifers đó là: unsigned, signed, short và long.',
            'typedef': 'Typedef (Tạm dịch: Định nghĩa kiểu dữ liệu) trong C++ là một từ khóa cho phép ta định nghĩa thêm tên mới cho các kiểu dữ liệu có sẵn\nCú pháp như sau: typedef <data_type> <new_name>',
            'constant': 'Constant hay const (Tạm dịch: Hằng số) trong C++ là một từ khóa dùng để chỉ định một biến hay một đối tượng (trong OOP) là một hằng - tức không thể làm thay đổi giá trị của nó kể từ sau khi khai báo từ khóa const.',
            'macro': 'Macro trong C++ là một trong các chỉ thị trong bộ tiền xử lý (Preprocessing), dùng để đặt lại tên của một chức năng, khối lệnh, giá trị,... theo ý của mình.\nCú pháp: #define <new_name> <a syntax, code block,...>\n Mình cũng có ví dụ như sau, giả sử mình muốn định nghĩa giá trị 3.14 có tên gọi là PI, mình có thể sử dụng macro như sau: #define PI 3.14',
            'wchar_t': 'wchar_t trong C++ là một kiểu dữ liệu wide character. Wide character khá giống với kiểu char ngoại trừ việc nó chiếm gấp đôi bộ nhớ và có thể một giá trị lớn hơn kiểu char (> 256)',
            'boolean': 'Boolean hay bool (Tạm dịch: Kiểu luận lý) trong C++ là một kiểu dữ liệu đại số luận lý chỉ gồm có hai giá trị là 0 (false) và 1 (true).',
            'data type': 'Data type (Tạm dịch: Kiểu dữ liệu) trong C++ là một hệ thống dùng để phân biệt sự khác nhau về lượng tài nguyên chiếm trong bộ nhớ và cách diễn giải mẫu bit của các biến hoặc các hàm.',
            'array': 'Array (Tạm dịch: Mảng) trong C++ là một kiểu dữ liệu, gồm một tập hợp các phần tử có cùng kiểu dữ liệu với nhau, được phân biệt bởi số thứ tự (index) bên trong mảng, bắt đầu từ vị trí 0.\nCú pháp: <data_type> <variable_name>[<size_of_array>];',
            'structure': 'Structure hay struct (Tạm dịch: Cấu trúc) trong C++ là một cú pháp dùng để biểu diễn một kiểu dữ liệu mới dựa vào việc tập hợp các biến cần thiết với nhau.\nCú pháp: struct <name>{\n//some variables;\n};',
            'class': 'Class (Tạm dịch: Lớp) trong C++ là một kiến thức liên quan đến Lập trình hướng đối tượng (Object Oriented Programming), là một bản thiết kế của các đối tượng có cùng chung các đặc điểm, tính chất, hành vi... Trong lập trình, một class có thể chứa các Biến - Thuộc tính (Attributes) và các Hàm - Phương thức (Methods).\nCú pháp: class <class_name>{\n//Some attributes\n//Some methods\n};\nĐể có thể hiểu rõ hơn về Class, bạn hãy tìm hiểu thêm về Lập trình hướng đối tượng nhé!',
            'union': 'Union (Tạm dịch: Hợp nhất) trong C++ là một cú pháp về cơ bản giống với struct, dùng để gom nhóm các biến lại với nhau để từ đó hình thành một kiểu dữ liệu mới.\nCú pháp: union <union_name>{\n//some variables\n};',
            'pointer': 'Pointer (Tạm dịch: Con trỏ) trong C++ là một biến chứa địa c hỉ của một biến khác với cùng kiểu dữ liệu đã được khai báo.\nCú pháp: <data_type>* <variable_name>;',
            'enumeration': 'Enumeration hay enum (Tạm dịch: Kiểu liệt kê) là một kiểu dữ liệu trong C++ dùng để định nghĩa một tập các hằng số cố định,',
            'integer': 'Integer hay int (Tạm dịch: Kiểu số nguyên) trong C++ là một kiểu dữ liệu cho phép lưu trữ những giá trị là số nguyên như -2,-1,0,1,...\nCú pháp: int <variable_name>;',
            'floating_point': 'Floating point hay float (Tạm dịch: Kiểu dấu chấm động/kiểu số thực) trong C++ là một kiểu dữ liệu cho phép lưu trữ các số có dạng -1.1234, 5.5467, 3.14,... Nói cách khác, kiểu dấu chấm động cho phép ta lưu trữ cả phần thập phân của một số.\nCú pháp: float <variable_name>;',
            'double': 'Double trong C++ là một kiểu dữ liệu ctrong C++ là một kiểu dữ liệu cho phép lưu trữ các số có dạng -1.1234, 5.5467, 3.14,... giống như kiểu float. Điểm khác biệt của double so với float nằm ở việc có miền giá trị lớn hơn.\nCú pháp: double <variable_name>;',
            'character': 'Character hay char (Tạm dịch: Kiểu kí tự) trong C++ là một kiểu dữ liệu dùng để lưu trữ một ký tự trong bảng mã ASCII như 1,2,3,a,b,c,d,... Kiểu char còn đặc biệt ở chỗ, nó vừa là kiểu kí tự nhưng cũng vừa là kiểu số nguyên (integer), chính vì thế ta cũng thể sử dụng số để đại diện cho các kí tự theo bảng mã ASCII khi làm việc với kiểu char.\nCú pháp: char <variable_name>;',
            'string': 'String (Tạm dịch: Kiểu chuỗi kí tự) trong C++ là một kiểu dữ liệu tập hợp các kí tự được đặt trong dấu ngoặc kép, dùng để biểu diễn một đoạn văn bản,... Lưu ý rằng kiểu string không phải là một kiểu dữ liệu được dựng sẵn trong C++ mà nó được cài đặt trong thư viện STL, vì vậy để sử dụng được string trước tiên các bạn cần phải khai báo: #include <string> cái đã nha!\nCú pháp: std::string <variable_name>;',
            'local variable': 'Local variables (Tạm dịch: Biến cục bộ) trong C++ là một biến được định nghĩa bên trong một khối lệnh. ',
            'global variable': 'Global variables (Tạm dịch: Biến toàn cục) trong C++ rheo quy ước được khai báo ở đầu của một tập tin, bên dưới #include. Chính vì được khai báo ngay đầu tập tin mà không nằm trong phạm vi của một khối lệnh nào nên biến toàn cục - đúng với tên gọi của nó sẽ có phạm vi hoạt động là toàn bộ tập tin code, tức là ta có thể sử dụng nó ở bất kì đâu mà ta muốn.',
            'auto': 'Auto (Tạm dịch: Tự động) trong C++ 11 là một kiểu dữ liệu cho phép nhận diện kiểu dữ liệu của một biến thông qua giá trị ta khởi tạo nó, ví dụ nếu ta khai báo: auto aStr = 10; thì kiểu dữ liệu của aStr lúc này sẽ là kiểu int',
            'external': 'External Variables (Tạm dịch: Biến ngoại) là biến mà có thể dùng chung ở các sourcefile khác nhau. Để có thể khai báo external variables, ta cần phải sử dụng từ khóa extern khi khai báo biến, và việc khai báo các external variables nên được thực hiện ở các header file (file .h) để tiện sử dụng.',
            'static': 'Static (Tạm dịch: Tĩnh) trong C++ là một từ khóa có thể sử dụng để khai báo chung với biến, hàm hoặc các thuộc tính, phương thức trong một class (OOP). Với biến static, dù đặt bên trong hay bên ngoài khối lệnh thì nó vẫn sẽ có hiệu lực - tức bất kì sự thay đổi giá trị ở đâu cũng làm biến static cập nhật đúng với giá trị đó - giống với Biến toàn cục (Global variable).',
            'vector': 'Vector trong C++ là một đối tượng có thể chứa một chuỗi các vùng nhớ liên tiếp nằm trong thư viện STL, đại diện cho kiểu Mảng (Array) thông thường.\nKhá giống với kiểu Mảng về chức năng, nhưng bên cạnh đó Vector còn cho thấy thêm một số điểm ưu việt hơn so với Array như việc không cần phải khai báo kích thước vì Vector có thể tự động tăng kích thước của nó lên, có thể biết được số lượng phần tử đang lưu bên trong nó hay có thể dùng được số phần tử âm,...',
            'reference variable': 'Reference variables (Tạm dịch: Biến tham chiếu) là một biến có các đặc điểm sau đây:\n_Biến tham chiếu không được cấp phát bộ nhớ, không có địa chỉ riêng.\n_Nó dùng làm bí danh cho một biến (kiểu giá trị) nào đó và nó sử dụng vùng nhớ của biến này.\nCú pháp: <data_type> &<variable_name> = <any_declared_variable>;',
            # Câu trả lời về các toán tử
            'decrement operator': '''Decrement operators (Tạm dịch: Toán tử giảm, Ký hiệu: --) là loại toán tử giảm giá trị của biến xuống 1 đơn vị, có thể đứng trước hoặc sau một biến và ở mỗi vị trí khác nhau sẽ có một số điểm khác biệt:\n
             _ Prefix decrement (Đứng trước biến): giảm giá trị của biến lên trước rồi cập nhật giá trị mới vào biến ngay lập tức.\n
             _ Postfix decrement (Đứng sau biến): sử dụng giá trị cũ của biến tại thời điểm dòng code đang thực thi cho đến khi tới dòng code tiếp theo thì mới cập nhật giá trị mới của biến (tức đã giảm 1)''',
            'increment operator': '''Increment operators (Tạm dịch: Toán tử tăng, Ký hiệu: ++) là loại toán tử tăng giá trị của biến lên 1 đơn vị, có thể đứng trước hoặc sau một biến và ở mỗi vị trí khác nhau sẽ có một số điểm khác biệt:\n
             _ Prefix increment (Đứng trước biến): tăng giá trị của biến lên trước rồi cập nhật giá trị mới vào x ngay lập tức.\n
             _ Postfix increment (Đứng sau biến): sử dụng giá trị cũ của biến tại thời điểm dòng code đang thực thi cho đến khi tới dòng code tiếp theo thì mới cập nhật giá trị mới của biến (tức đã tăng 1)''',
            'deference operator': '''Dereference operators (Tạm dịch: Toán tử trỏ, Ký hiệu: *) là loại toán tử cho phép chúng ta truy cập vào giá trị tại một địa chỉ cụ thể.''',
            'address_of operator': '''Address_of operators (Tạm dịch: Toán tử địa chỉ, Ký hiệu : &) là loại toán tử cho phép chúng ta lấy địa chỉ bộ nhớ của một biến.''',
            'comma operator': '''Comma operator (Tạm dịch: Toán tử phẩy, Ký hiệu : ,) là một loại toán tử cho phép ta kết nối các biểu thức lại với nhau, thực thi theo trình tự từ trái sang phải. Giả sử ta có đoạn code sau:\n
             int a = 0;\n
             int b = (a + 100, a++, a + 100);\n
             cout << b << endl ; // Kết quả là 201\n''',
            'ternary operator': 'Ternary operators (Tạm dịch: Toán tử ba ngôi, Ký hiệu: ? :) là toán tử có 3 toán hạng trong biểu thức. Cú pháp: (<condition_expression>) ? <value_if_true> : <value_if_false);\nTrong đó:\n_condition_expression: là một biểu thức điều kiện kiểu bool, thứ sẽ quyết định kết quả của phép toán.\n_value_if_true: Nếu biểu thức điều kiện trả về true, đây là sẽ là kết quả của phép toán.\n_value_if_false: Nếu biểu thức điều kiện trả về false, đây là sẽ kết quả của phép toán.',
            'binary operator': 'Binary operators (Tạm dịch: Toán tử hai ngôi) là toán tử có 2 toán hạng trong biểu thức. Có 5 toán tử số học 2 ngôi trong C++ đó là: Cộng (Addition : +), Trừ (Subtraction : -), Nhân (Multiplication : *), Chia lấy nguyên (Division : /), Chia lấy dư (Modulus : %)',
            'unary operator': 'Unary operators (Tạm dịch: Toán tử một ngôi) là toán tử chỉ có 1 toán hạng trong biểu thức. Ví dụ như việc bạn sử dụng dấu - để biểu diễn số âm kiểu -11, -60,...',
            'shift operator': 'Shift operators (Tạm dịch: Toán tử dời bit) bao gồm toán tử dời qua phải (right-shift - >>) và toán tử dời qua trái (left-shift - <<).',
            'bitwise operator': '''Bitwise operators (Tạm dịch: Toán tử bit) là toán tử họa động trên các bits và thực hiện các phép toán liên quan đến bit như &(AND), |(OR), ^(XOR), ~(One's complement), <<(Left shift), >>(Right shift).''',
            'logical operator': 'Logical operators (Tạm dịch: Toán tử logic) là loại toán tử dùng để kết hợp hai hay nhiều điều kiện lại với nhau để đánh giá và đưa ra kết quả cuối cùng. Ta có toán tử AND (&& - chỉ đúng khi tất cả điều kiện đều đúng), toán tử OR (|| - chỉ đúng khi một trong các điều kiện là đúng) và toán tử NOT(! - chỉ đúng khi kết quả cuối cùng của biểu thức là sai)',
            'comparison operator': 'Comparison operators hay Relational operators (Tạm dịch: Toán tử so sánh) là loại toán tử cho phép thực hiện các phép toán so sánh như so sánh hơn, so sánh bằng,...',
            'arithmetic operator': 'Arithmetic operators (Tạm dịch: Toán tử số học) là loại toán tử dùng để biểu diễn các phép toán số học như +,-,*,/,%...',
            'assignment operator': 'Assignment Operators (Tạm dịch: Toán tử gán, Ký hiệu: =) là một loại toán tử dùng để cấp phát giá trị',
            'operator': 'Operators (Tạm dịch: Toán tử) trong lập trình là một biểu tượng đại diện cho các phép toán số học như cộng trừ nhân chia hay các phép toán logic,... và trả về một kết quả. Trong C++, có rất nhiều loại toán tử nhưng cơ bản và chung nhất, ta có thể chia toán tử làm ba loại: Toán tử một ngôi (Unary Operator), Toán tử hai ngôi (Binary Operator) và Toán tử ba ngôi (Ternary Operator).',
            # Câu trả lời về control flow
            'if': 'If hay If statements (Tạm dịch: Lệnh if) là một lệnh được dùng để kiểm tra một biểu thức kiểu luận lý nào đó là đúng hay sai, nếu đúng thì sẽ thực thi tập chỉ thị bên trong khối if, nếu điều kiện sai thì sẽ bỏ qua khối lệnh if đó.\n Cú pháp: if(<boolean_expression>){\n//some codes here...\n}\nChi tiết hơn, Lệnh if còn được phân loại thành 4 loại: if, if else, if else if Ladder và nested if',
            'loop': 'Loop (Tạm dịch: Sự lặp) trong lập trình là một khái niệm dùng để chỉ sự lặp đi lặp lại một tập các chỉ thị (một khối lệnh) cho đến khi thỏa mãn điều kiện để dừng vòng lặp cho trước. Trong C++, một vòng lặp được đại diện bởi các từ khóa for (for loop), while (while loop) và do while(do while loop).',
            'control flow': 'Control flow hay Flow of control (Tạm dịch: Cấu trúc điều khiển) trong lập trình là một khái niệm dùng để chỉ một tập các chỉ thị, các lệnh hay các lời gọi hàm được thực thi khi chạy chương trình.',
            'selection statement': 'Selection statements (Tạm dịch: Lệnh lựa chọn) trong lập trình là một khái niệm dùng để chỉ sự quyết định thực thi một tập các chỉ thị hay một khối lệnh dựa dựa trên một điều kiện cho trước. Trong C++, ta có thể dùng lệnh if hoặc lệnh switch để có thể sử dụng lệnh lựa chọn.',
            'iteration statement': 'Iteration statements hay Loop (Tạm dịch: Lệnh lặp) trong lập trình là một khái niệm dùng để chỉ sự lặp đi lặp lại một tập các chỉ thị (một khối lệnh) cho đến khi thỏa mãn điều kiện để dừng vòng lặp cho trước. Trong C++, một vòng lặp được đại diện bởi các từ khóa for (for loop), while (while loop) và do while(do while loop)',
            'jump statement': 'Jump statements (Tạm dịch: Lệnh nhảy) trong lập trình là một khái niệm dùng để chỉ sự làm thay đổi đột ngột hướng thực thi code một cách vô điều kiện sang một tập chỉ khác ở một nơi nào đó trong tập tin code của chúng ta. Trong C++, ta có thể biểu diễn Lệnh nhảy bằng các lệnh gồm Lệnh break, Lệnh continue, Lệnh goto và Lệnh return.',
            'for': '''For hay For loops (Tạm dịch: Vòng lặp for) trong C++ là một cấu trúc vòng lặp với chức năng tương tự như vòng while nhưng khác về cú pháp. Cấu trúc của một vòng for như sau:\nfor(<loop_variable_declaration>;<stop_condition_expression>;<update_loop_variable_expression>){\n//Some codes here...\n
             }\nVới:\n
             _ loop_variable_declation: là nơi khởi tạo biến lặp, biến lặp được sử dụng như là một máy đếm số lần đã lặp của vòng for.\n
             _ stop_condition_expression: là nơi khởi tạo một biểu thức kiểu bool cho biến lặp, khi không còn thỏa mãn biểu thức này (false) thì vòng lặp sẽ kết thúc.\n
             _ update_loop_variable_expression: là nơi khởi tạo một biểu thức để cập nhật giá trị cho biến lặp sau mỗi lần lặp.''',
            'while': 'While hay While loops (Tạm dịch: Vòng lặp while) trong C++ là một vòng lặp với chức năng tương tự như vòng for nhưng khác về cú pháp. Cấu trúc của một vòng while như sau:\nwhile(<condition_expression>){\n//some codes here...\n}\nMình thể hiểu đơn giản cấu trúc đó như sau: trong khi điều kiện <condition_expression> vẫn trả về kết quả đúng (true), thì các đoạn code bên trong dấu { } vẫn sẽ được thực thi.',
            'do while': '''do while (Tạm dịch: Vòng lặp do while) trong C++ là một vòng lặp khá giống với vòng lặp while, điểm khác biệt ở do while so với while là nó sẽ đảm bảo vòng lặp sẽ được lặp ít nhất một lần.Cú pháp:\n
             do {\n
                // Some codes here;\n
            } while (<condition_expression>);''',
            'switch': '''Switch statements (Tạm dịch: Lệnh chuyển mạch) trong C++ giống như là một chuỗi các câu lệnh if else với việc so sánh một biến với các số nguyên. Cú pháp:\n
             switch (n)\n
            {\n
                case 1: // Sẽ thực thi khối lệnh ở đây nếu n == 1;\n
                        break;\n
                case 2: // Sẽ thực thi khối lệnh ở đây nếu n == 2;\n
                        break;\n
                default: // Nếu n không bằng với bất kì case nào thì sẽ thực thi khối lệnh ở đây;
            }''',
            'break': 'Break statements (Tạm dịch: Lệnh chấm dứt) trong C++ là một trong các lệnh nhảy, dùng để kết thúc một vòng lặp ngay lập tức kể cả khi nó vẫn còn có thể tiếp tục lặp.',
            'continue': 'Continue statements (Tạm dịch: Lệnh tiếp tục) trong C++ là một trong các lệnh nhảy, dùng để ép buộc trình biên dịch phải nhảy đến lần lặp kế tiếp của một vòng lặp.',
            'goto': '''Goto statements (Tạm dịch: Lệnh goto) trong C++ là một trong các lệnh nhảy, dùng để thực hiện việc đẩy trình biên dịch đến một đoạn code khác (label) và thực thi chúng. Cú pháp:\n
             // some code heres...;\n
             goto <label_name>;\n
            
             <label_name>:\n
             // some codes here;''',
            'if else': '''if else (Tạm dịch: Nếu không thì...) là một dạng đặc biệt của lệnh if khi mà ta có thể định nghĩa thêm một khối lệnh cho trường hợp biểu thức điều kiện sai.Ví dụ như sau:\n
             if(a == 1){\n
                // Some codes here;\n
             }\n
             else { // Nếu a != 1 thì sẽ thực thi đoạn code ở đây\n
                // Some code here;\n
             }''',
            'if else if ladder': '''if else if Ladder (Tạm dịch: Cầu thang if else) là một dạng đặc biệt của lệnh if khi ta định nghĩa thêm nhiều lệnh if hơn sau mỗi else. Ví dụ như sau:\n
             if(a == 1){\n
                // Some code heres;\n
             }\n
             else if (a == 2){\n
                // Some code heres;\n
             }\n
             else if (a == 3){\n
                // Some code heres;\n
             }''',
            'nested if': '''Nested if (Tạm dịch: if lồng if) là một dạng đặc biệt của lệnh if khi bên trong khối lệnh if lại có thêm một khối if khác nữa.Ví dụ như sau:\n
             if(a == 1){\n
                if(b == 2){ // Thêm một khối if nữa\n 
                    //Some codes here\n
                }\n
             }''',
            # Câu trả lời về function
            'function': 'Function (Tạm dịch: Hàm) là một đoạn các câu lệnh có thể tái sử dụng. Function cho phép lập trình viên cấu trúc chương trình thành những phân đoạn khác nhau để thực hiện những công việc khác nhau.',
            'parameter': 'Parameters (Tạm dịch: Tham số) là những gì chúng ta gọi khi định nghĩa một hàm. Parameter sẽ đại diện cho một giá trị mà hàm của bạn sẽ nhận được khi được gọi.',
            'argument': 'Arguments (Tạm dịch: Đối số) là đại diện cho giá trị truyền cho parameter khi chúng ta thực hiện lời gọi hàm. Mỗi argument sẽ tương ứng với một parameter khi khai báo.',
            'recursion': 'Recursion (Tạm dịch: Đệ quy) là một hàm tự gọi lại chính nó.',
            'pass by value': 'Pass by value (Tạm dich: Truyền tham trị) có thể được hiểu là giá trị của biến sẽ không bị thay đổi khi ta truyền biến này vào một hàm mà trong lúc thực thi đoạn code bên trong hàm có làm thay đổi giá trị của biến.',
            'pass by reference': 'Pass by reference (Tạm dịch: Truyền tham chiếu) có thể được hiểu là giá trị của biến sẽ bị thay đổi khi ta truyền biến này vào một hàm trong lúc thực thi đoạn code bên trong hàm có làm thay đổi giá trị của biến.',
            'return': 'Return keyword (Tạm dịch: Trả về) trong C++ là một từ khóa dùng để trả về một giá trị cho nơi gọi hàm, đây từ khóa bắt buộc đối với bất kì hàm nào được khai báo có giá trị trả về, và có thể có hoặc không đối với hàm khai báo kiểu void.',
            'return type': 'Return type (Tạm dịch: Kiểu trả về của hàm) trong C++ là việc định nghĩa kiểu giá trị mà hàm đó sẽ trả về cho nơi gọi hàm, giả sử ta khai báo một hàm kiểu int thì khi thực hiện lời gọi hàm, hàm này chắc chắn sẽ trả về một giá trị int.',
            'const reference': 'Const reference (Tạm dịch: Tham chiếu hằng) trong C++ là việc ta định nghĩa tham số truyền vào là tham chiếu với từ khóa const - tức là sẽ không thể thay đổi được giá trị của biến truyền vào hàm mặc dù đó là tham chiếu. Hiệu quả của việc sử dụng tham chiếu hằng chỉ thể hiện rõ khi làm việc với các đối tượng struct/class.',
            'inline function': 'Inline functions (Tạm dịch: Hàm nội tuyến) là một loại hàm trong ngôn ngữ lập trình C++. Từ khoá inline được sử dụng để đề nghị (không phải là bắt buộc) compiler (trình biên dịch) thực hiện inline expansion (khai triển nội tuyến) với hàm đó hay nói cách khác là chèn code của hàm đó tại địa chỉ mà nó được gọi.',
            'default value': 'Default values (Tạm dịch: Tham số mặc nhiên) là khi ta mặc định gán sẵn giá trị bất kì cho một tham số truyền vào khi thực hiện khai báo hàm. Điều đó đồng nghĩa, khi thực hiện lời gọi hàm mà không truyền vào đối số tương ứng, trình biên dịch sẽ sử dụng giá trị đã được gán sẵn cho tham số đó khi thực thi hàm.',
            'main function': 'Main function (Tạm dịch: Hàm main) trong C++ là một trường hợp của hàm, đây là nơi sẽ được thực thi đầu tiên khi chạy một chương trình C++.',
            'built in function': 'Built in functions (Tạm dịch: Hàm dựng sẵn) hay còn có tên gọi khác là Library functions, là các hàm ta có thể gọi nó trực tiếp mà không cần phải khai báo và định nghĩa chúng bởi vì chúng đã được viết sẵn trong các thư viện của C++ như thư viện stdio.h, iostream,...'
        }

        if cplusplus_content in all_answers_what and curr_intent == 'c++_what_asking':
            cplusplus_content_answer = all_answers_what[cplusplus_content]
        dispatcher.utter_message(text=cplusplus_content_answer)

        return [SlotSet("cplusplus_content_answer", cplusplus_content_answer)]


class ValidateCppContentForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_cpp_content_form"

    @staticmethod
    def cpp_content_db() -> List[Text]:
        """Database of supported c++ content"""

        return ['library',
                'namespace',
                'cplusplus',
                'comment',
                'include',
                'unsigned',
                'singed',
                'short',
                'long',
                'type modifier',
                'typedef',
                'constant',
                'macro',
                'wchar_t',
                'boolean',
                'data type',
                'variable',
                'array',
                '2d array',
                'structure',
                'class',
                'union',
                'pointer',
                'enumeration',
                'integer',
                'floating_point',
                'double',
                'character',
                'string',
                'local variable',
                'global variable',
                'auto',
                'external',
                'static',
                'vector',
                'deference operator',
                'reference operator',
                'comma operator',
                'ternary operator',
                'binary operator',
                'unary operator',
                'shift operator',
                'bitwise operator',
                'logical operator',
                'comparison operator',
                'arithmetic operator',
                'assignment operator',
                'operator',
                'if',
                'loop',
                'control flow',
                'control statement',
                'selection statement',
                'iteration statement',
                'jump statement',
                'for',
                'while',
                'do while',
                'switch',
                'break',
                'continue',
                'goto',
                'if else',
                'if else if ladder',
                'nested if',
                'function',
                'parameter',
                'argument',
                'recursion',
                'pass by value',
                'pass by reference',
                'return',
                'return type',
                'const reference',
                'inline function',
                'default value',
                'main function',
                'built in function']

    def validate_cpp_content(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate cuisine value."""

        if slot_value.lower() in self.cpp_content_db():
            # validation succeeded, set the value of the "c++_content" slot to value
            return {"c++_content": slot_value}
        else:
            # validation failed, set this slot to None so that the
            # user will be asked for the slot again
            return {"c++_content": None}


'''
class CppContentForm(FormValidationAction):
    def name(self) -> Text:
        """identifier của form """
        return 'cpp_content_form_validation'

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
'''

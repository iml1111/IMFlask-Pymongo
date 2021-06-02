# IMFlask-Pymongo
**Boilerplate for Large Scale Flask Web Backend Structure with PyMongo (Edited 2021-06-02)**

Flask를 사용하여 대규모 어플리케이션 서버를 구축한다고 가정했을 때의 Baseline 코드입니다.

해당 코드는 Flask + Pymongo의 조합에 특화되어 있습니다.

여러 오픈 소스를 읽어보고 제 몸에 와닿는 직관적인 부분만 반영한 것이라 부족한 점이 많습니다.

피드백은 적극적으로 환영합니다.



# Concept

### Application Factory

어플리케이션은 개발(development), 테스팅(Testing), 상용(Production) Level에서 다르게 동작해야 합니다. 따라서 실행하고자 하는 환경에 따라 config를 다르게 주입시키는 애플리케이션 팩토리를 구현했습니다.



### Flask Extension을 지양하자

Flask extension는 유용하지만 몇가지 문제가 있다고 생각했습니다.

- 몇몇 extension은 업데이트가 되지 않고 있습니다. 대표적으로 많은 Flask open source에서 사용하고 있는 **flask_script**가 그렇습니다. 
- 확실히 쓰면 편리하지만, 몇몇 package는 오히려 자체의 rule을 강요받는다는 느낌이 들었습니다.
  저의 생각과 일치하거나, 제가 직접 구현이 불가능한 수준이 아니라면 굳이 확장 패키지**(flask_moment, flask-restful 등)**를 사용하지 않았습니다.

따라서 Flask 및 Python 자체에서 기본적으로 지원하는 기능을 충실히 활용하도록 노력했습니다.
**(함께 import 되어 있는 flask-validation-extended는 제가 만든거라 넣어봤습니다 ㅎㅎ)**



### 모든 모듈은 각각 독립적으로 실행이 가능해야 한다






### 저수준의 DB 드라이버를 사용하자

모든 DB단 연동 코드에는 **ORM, ODM과 같은 Database Abstraction Module을 사용하지 않았습니다.**

당연히 Large Scale이라면, Abstraction을 사용하는게 보편적이지만, 저는 공부하는 입장에서 제가 직접 DB까지 전달되는 처리를 가능한 한 자세하게 관여할 수 있도록 구조를 구현하였습니다.

또한 저 자신이 공부가 부족해서인지 아직, 이러한 Abstraction에 대한 중요성이 와닿지 않아서 적용시키지 않았습니다.



### 딱히 REST API는 아닙니다

제가 들은 지식을 바탕으로 가능한한 RESTful스럽게 구현을 해보긴 했습니다만, 역시나 얕게 들은 지식인 만큼 완전하지 않습니다. 다만, 적어도 아래와 같은 규약을 적용해보았습니다.

- 모든 API는 **GET, POST, PUT, DELETE 내에서 규격화하여 url을 단축**시켰습니다.
- 모든 API의 **request/response의 data tranfer format은 JSON으로 일관적으로 처리**하였습니다.

후에 파일 업로드 처리는 어떻게 할 것이냐는 숙제가 남아있습니다만, 이 경우 예외적으로 multipart/form-data을 활용하거나 다른 방안을 생각해봐야 할 것 같습니다.



### Flask Extended 적용


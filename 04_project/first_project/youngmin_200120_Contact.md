# JAVA
```java
package run;

import main.ContactMain; //다른 패키지에 있는 클래스 import

public class ContactRun {

public static void main(String[] args) {
ContactMain run = new ContactMain(); //ContactMain클래스 new
run.run(); //실행
}

}


package main;

import java.util.ArrayList; //필요한 클래스 import
import java.util.HashMap;
import java.util.Iterator;
import java.util.Scanner;
import java.util.Set;



public class ContactMain { //메인화면 출력


private Scanner scanner = new Scanner(System.in); //스캐너 new
private HashMap<String,String> person = new HashMap<String,String>();// 안쪽 해쉬맵선언
private HashMap<String,HashMap<String,String>> all = //바깥쪽 해쉬맵 선언
new HashMap<String,HashMap<String,String>>();
private Set<String> akeys = all.keySet();  //바깥해쉬맵 키들
private HashMap<String,String>avalue=all.get(akeys); //안쪽 해쉬맵들

public void ShowMainMenu(){ //메인화면 출력

System.out.println();
System.out.println("===========================");
System.out.println("    다음 메뉴 중 하나를 선택하세요.");
System.out.println("===========================");
System.out.println("1. 회원 추가");
System.out.println("2. 회원 목록 보기");
System.out.println("3. 회원 정보 수정하기");
System.out.println("4. 회원 삭제");
System.out.println("5. 종료");
System.out.println();
}
public void run(){
int select; //선택 번호 입력받는 select변수 선언
boolean run = true; //반복문을 위한 boolean형 변수 run선언

while(run) { //반복문 시작
do {
ShowMainMenu(); //메인화면 출력
select = scanner.nextInt(); //선택값 받기
}while((select<1)||(select>5)); //예외값일때 다시 입력받기

switch(select) { //스위치문 사용하여 선택값 입력
case 1: //1.회원 추가
insertContact();
break;
case 2: //2.회원 목록 보기
showContact();
break;
case 3: //3.회원 정보 수정하기
modifyContact();
break;
case 4: //4.회원 삭제
deleteContact();
break;
case 5: //5.종료
System.out.println("종료되었습니다.");
run = false;
break;
}
}
}


String name=null; //입력값 받을 변수 선언
String phone=null;
String division=null;

private void insertContact() {//입력
System.out.println();
System.out.println("등록할 회원의 정보를 입력하세요.");
System.out.print("이름 : ");
name = scanner.next(); //입력값 받기
System.out.print("전화번호(ex: 01012345678): ");
phone = scanner.next();
System.out.print("구분(ex.가족, 친구, 회사, 기타): ");
division = scanner.next();

person.put("이름",name); //입력받은 값들 안쪽 해쉬맵에 삽입
person.put("전화번호",phone);
person.put("구분",division);

all.put(phone, person); //안쪽해쉬맵을 연락처를 key로 잡아 바깥쪽 해쉬맵에 삽입

person=new HashMap<>(); //다음 값을 받기 위해 안쪽 해쉬맵을 재생성
}

private void showContact() {// 전체출력

Iterator<String> it = akeys.iterator(); //바깥쪽 해쉬맵 키들을 저장한 akeys Iterator처리한 it변수 선언
System.out.println("총 "+ all.size() +"명의 회원이 저장되어 있습니다."); //바깥쪽 해쉬맵의 포함된 요소의 갯수를 반환하는 size메소드 사용

while(it.hasNext()) { //반복문시작 - hasNext메소드사용하여 해쉬맵 바깥쪽 키들을 가지고 있는 it변수에 다음값이 없을때 까지 반복
String key = it.next(); //it변수에 다음값을 저장하는 key변수 선언
HashMap<String,String>value=all.get(key);
//바깥쪽 해쉬맵에서 key변수에 들어있는 연락처들(바깥쪽 해쉬맵의 Key)과 매칭되는 value들(안쪽 해쉬맵들)을 저장하는 value해쉬맵 선언

System.out.print("회원정보 : ");
System.out.print("이름 = "+value.get("이름")+", ");
System.out.print("전화번호 = "+value.get("전화번호")+", ");
System.out.println("구분 = "+value.get("구분"));
//value해쉬맵에서 이름,연락처, 구분 출력(akeys에 바깥쪽 해쉬맵의 Key값들이 모두 들어있기 때문에 전체출력이 가능하다.)
}
}

private void modifyContact() {//수정
ArrayList<String>keylist = new ArrayList<String>(); //keylist어레이리스트 선언
Iterator<String> it = akeys.iterator(); //바깥쪽 해쉬맵 키들을 저장한 akeys Iterator처리한 it변수 선언
System.out.println("수정할 회원의 이름을 입력하세요.");
System.out.println("이름 : ");
String name2 = scanner.next(); //수정할 회원의 이름을 받는 name2변수 선언

while(it.hasNext()) { //반복문 시작 - hasNext메소드사용하여 해쉬맵 바깥쪽 키들을 가지고 있는 it변수에 다음값이 없을때 까지 반복
String key = it.next(); //it변수에 다음값을 저장하는 key변수 선언
HashMap<String,String> value = all.get(key);
//바깥쪽 해쉬맵에서 key변수에 들어있는 연락처들(바깥쪽 해쉬맵의 Key)과 매칭되는 value들(안쪽 해쉬맵들)을 저장하는 value해쉬맵 선언

if(value.get("이름").equals(name2)) { //if문 - 입력받은 이름과 안쪽해쉬맵의 '이름'과 같은것이 있으면
keylist.add(key); //해당 Key값을 keylist어레이리스트에 추가
}
}
if(keylist.isEmpty()) { //if문 - 입력받은 이름과 안쪽해쉬맵의 '이름'과 같은것이 있다면 해당 Key값을 넣는 keylist어레이리스트 이므로 비어있다면
System.out.println("입력하신 이름이 존재하지 않습니다."); //입력받은 이름이 존재하지 않는다는 경고문 출력
}else { //입력받은 이름이 keylist어레이리스트에 존재할경우
System.out.println("총 "+keylist.size()+"개의 목록이 검색되었습니다.");
//keylist어레이리스트의 요소갯수를 출력하는 size메소드를 이용해 총 갯수 출력(keylist에 들어있는 요소갯수는 입력받은 이름과 매칭되는 갯수)
System.out.println("아래 목록 중 수정할 회원의 번호를 입력하세요.");

for(int i=0; i<keylist.size();i++) { //for문 반복문 - keylist의 요소갯수만큼 반복되는 반복문 설정
String Inputkey = keylist.get(i); //keylist의 i번째 index를 추출하여 저장하는 Inputkey변수 선언

HashMap<String,String>Inputvalue = all.get(Inputkey);
//바깥쪽 해쉬맵에서 Inputkey에 저장되어있는 연락처를 Key로 하는 value들(안쪽해쉬맵 중에서 입력받은 이름과 매칭되는
//연락처를 Key값으로 가진 해쉬맵들)을 저장하는 Inputvalue해쉬맵 선언

System.out.print((i+1)+"."); //번호출력
System.out.print("이름 = "+Inputvalue.get("이름")+", ");
System.out.print("전화번호 : "+Inputvalue.get("전화번호")+", ");
System.out.println("구분 : "+Inputvalue.get("구분"));
//입력받은 이름과 매칭되는 Inputvalue 연락처를 Key값으로 가진 해쉬맵들의 요소들 출력
}

int num1 = scanner.nextInt(); //번호를 입력받을 num1변수 선언
all.remove(keylist.get(num1-1));
//입력받은 이름과 매칭되는 Key값들을 가진 keylist어레이리스트에서 입력받은 번호-1(index값)을 추출하여 바깥쪽 해쉬맵에서 해당 해쉬맵 삭제
System.out.println("수정할 정보를 입력하세요.");
System.out.print("이름: ");
String name = scanner.next(); //수정할 정보 받기
System.out.println("전화번호(ex: 01012345678): ");
String phone = scanner.next();
System.out.println("구분(ex.가족, 친구, 기타): ");
String division = scanner.next();

person.put("이름",name); //수정할 정보를 안쪽해쉬맵에 삽입
person.put("전화번호",phone);
person.put("구분",division);

all.put(keylist.get(num1-1),person); //수정할 정보를 가지고있는 안쪽해쉬맵을 삭제한 곳에 삽입

person=new HashMap<>(); //다음 값을 받기 위해 안쪽 해쉬맵을 재생성

System.out.println("수정이 완료되었습니다.");

}
}




private void deleteContact() { //삭제
ArrayList<String>keylist = new ArrayList<String>(); //keylist어레이리스트 선언
Iterator<String> it = akeys.iterator(); //바깥쪽 해쉬맵 키들을 저장한 akeys Iterator처리한 it변수 선언

System.out.println("삭제할 회원의 이름을 입력하세요.");
System.out.println("이름 : ");
String name2 = scanner.next(); //삭제할 회원의 이름 값 받는 name2변수 선언


while(it.hasNext()) { //반복문 시작 - hasNext메소드사용하여 해쉬맵 바깥쪽 키들을 가지고 있는 it변수에 다음값이 없을때 까지 반복
String key = it.next(); //it변수에 다음값을 저장하는 key변수 선언
HashMap<String,String> value = all.get(key);
//바깥쪽 해쉬맵에서 key변수에 들어있는 연락처들(바깥쪽 해쉬맵의 Key)과 매칭되는 value들(안쪽 해쉬맵들)을 저장하는 value해쉬맵 선언

if(value.get("이름").equals(name2)) { //if문 - 입력받은 이름과 안쪽해쉬맵의 '이름'과 같은것이 있으면
keylist.add(key); //해당 Key값을 keylist어레이리스트에 추가
}
}
if(keylist.isEmpty()) { //if문 - 입력받은 이름과 안쪽해쉬맵의 '이름'과 같은것이 있다면 해당 Key값을 넣는 keylist어레이리스트 이므로 비어있다면
System.out.println("입력하신 이름이 존재하지 않습니다."); //입력받은 이름이 존재하지 않는다는 경고문 출력
}else { //입력받은 이름이 keylist어레이리스트에 존재할경우
System.out.println("총 "+keylist.size()+"개의 목록이 검색되었습니다.");
//keylist어레이리스트의 요소갯수를 출력하는 size메소드를 이용해 총 갯수 출력(keylist에 들어있는 요소갯수는 입력받은 이름과 매칭되는 갯수)
System.out.println("아래 목록 중 삭제할 회원의 번호를 입력하세요.");

for(int i=0; i<keylist.size();i++) { //for문 반복문 - keylist의 요소갯수만큼 반복되는 반복문 설정
String Inputkey = keylist.get(i); //keylist의 i번째 index를 추출하여 저장하는 Inputkey변수 선언
HashMap<String,String>Inputvalue = all.get(Inputkey);
//바깥쪽 해쉬맵에서 Inputkey에 저장되어있는 연락처를 Key로 하는 value들(안쪽해쉬맵 중에서 입력받은 이름과 매칭되는
//연락처를 Key값으로 가진 해쉬맵들)을 저장하는 Inputvalue해쉬맵 선언

System.out.print((i+1)+"."); //번호출력
System.out.print("이름 = "+Inputvalue.get("이름")+", ");
System.out.print("전화번호 : "+Inputvalue.get("전화번호")+", ");
System.out.println("구분 : "+Inputvalue.get("구분"));
//입력받은 이름과 매칭되는 Inputvalue 연락처를 Key값으로 가진 해쉬맵들의 요소들 출력
}
int num1 = scanner.nextInt(); //번호를 입력받을 num1변수 선언
all.remove(keylist.get(num1-1));
//입력받은 이름과 매칭되는 Key값들을 가진 keylist어레이리스트에서 입력받은 번호-1(index값)을 추출하여 바깥쪽 해쉬맵에서 해당 해쉬맵 삭제
System.out.println("삭제가 완료되었습니다.");
}
}

}
```
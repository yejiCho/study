# Contact


```java



package FirstTeamWork;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Scanner;
import java.util.Set;

public class Contact {

public static void main(String[] args) {

// 전체 회원이 들어갈 해쉬맵
HashMap<String, HashMap<String, String>> allmember =
new HashMap<String, HashMap<String, String>>();

Scanner scanner = new Scanner(System.in);


// 전체 반복문 시작
boolean flag = true;
while(flag) {

// 메뉴
System.out.println("========================");
System.out.println("   다음 메뉴 중 하나를 선택하세요.  ");
System.out.println("========================");
System.out.println("1. 회원 추가");
System.out.println("2. 회원 목록 보기");
System.out.println("3. 회원 정보 수정하기");
System.out.println("4. 회원 삭제");
System.out.println("5. 종료");
int n = scanner.nextInt();


// 1~4에 해당하는 반복문 시작
switch(n) {
// 1. 회원 추가
case 1:
// 회원 개개인의 정보가 들어갈 해쉬맵
HashMap<String, String> member = new HashMap<String, String>();
System.out.println("등록할 회원의 정보를 입력하세요.");
System.out.print("이름:");
String m = scanner.next(); // 회원 이름 입력
member.put("이름", m);
System.out.println("전화번호(ex: 01012345678) :");
String pn = scanner.next();
member.put("전화번호", pn);
System.out.println("구분(ex: 가족, 친구, 기타) :");
String relation = scanner.next();
member.put("구분", relation);

allmember.put(pn, member);

break;

// 2. 회원 목록 보기
case 2:
int amn = allmember.size(); // 전체 회원의 수
System.out.println("총 " + amn + "명의 회원이 저장되어 있습니다.");
Set<String> keys = allmember.keySet(); // 전체 회원들의 정보 출력
Iterator<String> it = keys.iterator();
while(it.hasNext()) {
String key = it.next();
HashMap<String, String> am = allmember.get(key);
System.out.println("회원정보 : 이름 = " + am.get("이름") + ", "
+ "전화번호 : " + am.get("전화번호") + ", "
        + "구분 : " + am.get("구분"));
}
break;
// 3. 회원 정보 수정하기
case 3:
System.out.println("수정할 회원의 이름을 입력하세요.");
System.out.println("이름 : ");
String un = scanner.next();
ArrayList<String> ul = new ArrayList<String>();
Set<String> key = allmember.keySet(); // 검색한 회원들의 정보 출력
Iterator<String> ite = key.iterator();
while(ite.hasNext()) {
String keyss = ite.next();
HashMap<String, String> delete = allmember.get(keyss);
if(delete.get("이름").equals(un)) {
ul.add(keyss);
  }
  }

if(ul.isEmpty()) {
System.out.println("해당하는 회원 정보가 없습니다.");
}else {
System.out.println("총" + ul.size() + "개의 목록이 검색 되었습니다.");
System.out.println("아래 목록 중 수정할 회원의 번호를 입력하세요.");

for(int i = 0; i < ul.size(); i++) {
String deletename = ul.get(i);

HashMap<String, String> delete = allmember.get(deletename);

System.out.println((i+1)+ "." + "회원정보 : 이름 = " + delete.get("이름") + ", "
+ "전화번호 : " + delete.get("전화번호") + ", "
+ "구분 : " + delete.get("구분"));

}
HashMap<String, String> membert = new HashMap<String, String>();
int deleteindex = scanner.nextInt();
allmember.remove(ul.get(deleteindex-1));
System.out.println("수정할 회원의 정보를 입력하세요.");
System.out.print("이름:");
String mt = scanner.next();
membert.put("이름", mt);
System.out.println("전화번호(ex: 01012345678) :");
String pnt = scanner.next();
membert.put("전화번호", pnt);
System.out.println("구분(ex: 가족, 친구, 기타) :");
String relationt = scanner.next();
membert.put("구분", relationt);

allmember.put(pnt, membert);
System.out.println("수정이 완료되었습니다.");

}
break;
 

// 4. 회원 삭제
case 4:
System.out.println("삭제할 회원의 이름을 입력하세요.");
System.out.println("이름 : ");
String dn = scanner.next();
ArrayList<String> dl = new ArrayList<String>();
Set<String> kei = allmember.keySet();
Iterator<String> itee = kei.iterator();
while(itee.hasNext()) {
String keysss = itee.next();
HashMap<String, String> update = allmember.get(keysss);
if(update.get("이름").equals(dn)) {
dl.add(keysss);
  }
  }

if(dl.isEmpty()) {
System.out.println("해당하는 회원 정보가 없습니다.");
}else {
System.out.println("총" + dl.size() + "개의 목록이 검색 되었습니다.");

for(int i = 0; i < dl.size(); i++) {
String updatename = dl.get(i);

HashMap<String, String> update = allmember.get(updatename);

System.out.println((i+1)+ "." + "회원정보 : 이름 = " + update.get("이름") + ", "
+ "전화번호 : " + update.get("전화번호") + ", "
+ "구분 : " + update.get("구분"));
}

System.out.println("아래 목록 중 삭제할 회원의 번호를 입력하세요.");
int updateindex = scanner.nextInt();
allmember.remove(dl.get(updateindex-1));
System.out.println("삭제가 완료되었습니다.");
}
break;

 

// 5. 종료
case 5:
flag = false;
System.out.println("종료되었습니다.");
scanner.close();
break;
 }    
 }

 }
}   


```

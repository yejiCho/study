# java 연락처 프로그램

```java

//main class
package main;

import java.util.Scanner;
import main.ContactNm;

public class CollectionContact {

	public static void main(String[] args) {
		
		Scanner scanner = new Scanner(System.in);
		
		while(true) {
			System.out.println("\n =============== \n"
						+"다음 메뉴 중 하나를 선택하세요."
						+"\n =============== \n");
			System.out.println("1. 회원추가");
			System.out.println("2. 회원 목록 보기");
			System.out.println("3. 회원 목록 수정하기");
			System.out.println("4. 회원 삭제하기");
			System.out.println("5. 종료하기");
			
			System.out.print(">>  ");
			String text = scanner.next();
			
			if(text.equals("1")) {
				
				ContactNm.Input();
				
				
			}else if(text.equals("2")) {
				
				ContactNm.List();
			
			}else if(text.equals("3")) {
			
				ContactNm.revise();
				
			}else if(text.equals("4")) {
				
				ContactNm.delete();
				
			}else if(text.equals("5")) {
				
				System.out.println("종료되었습니다.");
				break;
				
			}else {
				
				System.out.println("해당하는 번호가 없습니다.");
			}
			
		}
	}

}


```


```java

	package main;
	
	import java.util.ArrayList;
	import java.util.HashMap;
	import java.util.Iterator;
	import java.util.Scanner;
	import java.util.Set;
	// class 분할 ContactNm class
	public class ContactNm {
		//PrivateInfo HashMap :  각각의 쌍에다가 "이름", "전화번호" , "구분" 키 생성후 value값 put
		//TotalInfo HashMap : Key값: 전화번호, Value값 : PrivateInfo 
		static HashMap<String, String> PrivateInfo = new HashMap<String,String>();
		static HashMap<String, HashMap<String, String>> TotalInfo = new HashMap<String, HashMap<String, String>>();
		static Scanner sc = new Scanner(System.in);
		
		public static void Input() {
			
			PrivateInfo = new HashMap<String, String>();
			System.out.print("이름 : ");
			
			String name = sc.next();
			PrivateInfo.put("이름", name);
			
			System.out.print("전화번호 : ");
			String phonenm = sc.next();
			PrivateInfo.put("전화번호", phonenm);
			
			System.out.print("구분(ex:가족, 친구, 회사, 기타): ");
			String classification = sc.next();
			PrivateInfo.put("구분", classification);
			
			TotalInfo.put(phonenm, PrivateInfo);
			
			
		}
		
		public static void List() {
			
			int n = TotalInfo.size();
			Set<String> keys = TotalInfo.keySet();
			Iterator<String> it = keys.iterator();
			System.out.println("총"
							+ n
							+"명의 회원이 저장되어 있습니다.");
			while(it.hasNext()) {
				String key = it.next();
				System.out.println("회원 정보: "
						+ "이름 = " + TotalInfo.get(key).get("이름")
						+ ", 전화번호 = " + TotalInfo.get(key).get("전화번호")
						+ ", 구별 = " +	TotalInfo.get(key).get("구분"));
				
			}
		}
		
		public static void revise() {
			
			PrivateInfo = new HashMap<String, String>();
			
			System.out.println("수정할 회원의 이름을 적으세요.");
		
			String rename = sc.next();
			Iterator<String> it = TotalInfo.keySet().iterator();
			ArrayList<String> ContactNm = new ArrayList<String>();
			
			while(it.hasNext()) {
				String key = it.next();
				if(rename.equals(TotalInfo.get(key).get("이름"))) {
					
					ContactNm.add(key);
					
				}
			}
			System.out.println("총"+ ContactNm.size()+"회원이 검색되었습니다.");
			
			if(ContactNm.isEmpty()) {
				
				System.out.println("일치하는 회원이 없습니다.");
				
			}else {
				
				System.out.println("아래 목록 중 수정할 회원의 번호를 입력하세요");
				for(int i = 0; i < ContactNm.size(); i++) {
					
					String key = ContactNm.get(i);
					
					System.out.println((i+1) + "이름: " + TotalInfo.get(key).get("이름")
								+ TotalInfo.get(key).get("전화번호")
								+ TotalInfo.get(key).get("구분"));
					
				}
				
				int renum = sc.nextInt();
				
					String getnum = ContactNm.get(renum - 1);
					TotalInfo.remove(getnum);
					
					System.out.print("이름: ");
					String name = sc.next();
					PrivateInfo.put("이름", name);
				
					System.out.print("전화번호: ");
					String phonenum = sc.next();
					PrivateInfo.put("전화번호", phonenum);
				
					System.out.print("구분: ");
					String classification = sc.next();
					PrivateInfo.put("구분", classification);
					
					TotalInfo.put(phonenum, PrivateInfo);
			}
			
		}
		
		public static void delete() {
			
			System.out.println("삭제할 회원의 이름을 입력하세요.");
			System.out.print("이름: ");
			String delname = sc.next();
			Iterator<String> it = TotalInfo.keySet().iterator();
			ArrayList<String> contactnum = new ArrayList<String>();
			
			while(it.hasNext()) {
				
				String key = it.next();
				
				if(delname.equals(TotalInfo.get(key).get("이름"))) {
					
					contactnum.add(key);
					
				}
			}
			
			System.out.println("총" + contactnum.size() + "명의 회원이 검색되었습니다.");
			
			if(contactnum.isEmpty()) {
				
				System.out.println("일치하는 회원이 없습니다.");
				
			}else {
				
				System.out.println("아래 목록 중 삭제할 회원의 번호를 입력하세요.");
				
				for(int i = 0; i < contactnum.size(); i++) {
					
					String key = contactnum.get(i);
					System.out.println((i+1) +"이름: " + TotalInfo.get(key).get("이름")
								+ "전화번호 : " + TotalInfo.get(key).get("전화번호")
								+ "구분: "+ TotalInfo.get(key).get("구분"));
					
				}
				
				int delnum = sc.nextInt();
				
				String getNum = contactnum.get(delnum-1);
				TotalInfo.remove(getNum);
				System.out.println("삭제되었습니다.");
				

			}
			
			
		}
	}
	



```
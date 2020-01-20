# java

## qwe

```java
package main;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Scanner;
import java.util.Set;

public class exex {
	public static void main(String[] args) {
		
		Scanner scanner = new Scanner(System.in);
		
		HashMap<String, HashMap<String,String>> nm = new HashMap<String, HashMap<String,String>>();
		

		int key = 0;
		
		while(true) {
			System.out.println("==========================");
			System.out.println("  다음 메뉴 중 하나를 선택하세요.");
			System.out.println("==========================");
			System.out.println("1. 회원 추가 ");
			System.out.println("2. 회원 목록 보기 ");
			System.out.println("3. 회원 정보 수정하기 ");
			System.out.println("4. 회원 삭제 ");
			System.out.println("5. 종료 ");
			
			key = scanner.nextInt();
//		종료
			if(key == 5) {
			System.out.println("종료되었습니다.");
			break;
//		회원 추가
			}else if(key == 1) {
				HashMap<String, String> personnm = new HashMap<String, String>();
				System.out.println("등록할 회원의 정보를 입력하세요.");
				System.out.print("이름 : ");
				String name = scanner.next();
				personnm.put("name", name);
				System.out.print("전화번호(ex 01012345678): ");
				String number = scanner.next();
				personnm.put("number", number);
				System.out.print("구분(ex. 가족, 친구, 기타):  ");
				String classfy = scanner.next();
				personnm.put("classfy", classfy);
				nm.put(number,personnm);
	
//		회원 목록보기
			}else if(key ==2) {
				System.out.println("총 " + nm.size() + "명의 회원이 저장되어 있습니다." );
				Set<String>keys= nm.keySet();
				Iterator<String> iterator = keys.iterator();
				while(iterator.hasNext()) {
					
					String number = iterator.next();
					HashMap<String, String> value = nm.get(number);
					
					System.out.println("회원정보 : " + "이름  = " +value.get("name")  + " 전화번호  : " + value.get("number") + " 구분 : " +value.get("classfy") );
				}
//		회원 정보 수정하기
			}else if(key ==3 ) {
				System.out.println("수정할 회원의 이름을 입력하세요.");
				System.out.println("이름 : ");
				String name= scanner.next();
				ArrayList<String> Samenm = new ArrayList<String>();
				Set<String>keys= nm.keySet();
				Iterator<String> iterator = keys.iterator();
				while(iterator.hasNext()) {
					String number = iterator.next();
					HashMap<String, String> match = nm.get(number);
					if(match.get("name").equals(name)){
						Samenm.add(number);	
					}					
				}
				
				if(Samenm.isEmpty()) {
					System.out.println("없어요 다시적어요");
				}else {
					
					System.out.println("총 " + Samenm.size()+"개의 목록이 검색되었습니다.");
					System.out.println("아래 목록중 수정할 회원의 번호를 입력하세요.");
					for(int i=0; i <Samenm.size(); i++ ) {					
						String matchname = Samenm.get(i);
						HashMap<String, String> match = nm.get(matchname);
						System.out.println((i+1) +"." + "이름  = " + match.get("name")  + " 전화번호  : " + match.get("number") + " 구분 : " + match.get("classfy"));
					}
					HashMap<String, String> personnm = new HashMap<String, String>();
					int matchindex= scanner.nextInt();
					nm.remove(Samenm.get(matchindex-1));
					System.out.println("수정할 정보를 입력하세요");
					System.out.print("이름 : ");
					String names = scanner.next();
					personnm.put("name", names);
					System.out.print("전화번호 : ");
					String number = scanner.next();
					personnm.put("number", number);
					System.out.print("구분 : ");
					String classfy = scanner.next();
					personnm.put("classfy", classfy);
					nm.put(number,personnm);
					System.out.println("수정이 완료되었습니다.");
				
					
				}	
//		회원정보 삭제하기
			}else if(key ==4) {
				System.out.println("삭제할 회원의 이름을 입력하세요.");
				System.out.println("이름 : ");
				String name= scanner.next();
				ArrayList<String> Samenm = new ArrayList<String>();
				Set<String>keys= nm.keySet();
				Iterator<String> iterator = keys.iterator();
				while(iterator.hasNext()) {
					String number = iterator.next();
					HashMap<String, String> match = nm.get(number);
					if(match.get("name").equals(name)){
						Samenm.add(number);	
					}					
				}
				
				if(Samenm.isEmpty()) {
					System.out.println("없어요 다시적어요");
				}else {
					
					System.out.println("총 " + Samenm.size()+"개의 목록이 검색되었습니다.");
				
				
					for(int i=0; i <Samenm.size(); i++ ) {					
						String matchname = Samenm.get(i);
						HashMap<String, String> match = nm.get(matchname);
						System.out.println((i+1) +"." + "이름  = " + match.get("name")  + " 전화번호  : " + match.get("number") + " 구분 : " + match.get("classfy"));
					}
					System.out.println("아래 목록 중 삭제할 회원의 번호를 입력하세요.");
					int matchindex= scanner.nextInt();
					nm.remove(Samenm.get(matchindex-1));
					System.out.println("삭제가 완료되었습니다.");
				}
			}				
		}	scanner.close();
	}
}


```



```java

package main;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Scanner;
import java.util.Set;

public class Contact {

	public static void main(String[] args) {

		HashMap<String, HashMap<String, String>> ALHM =	
											new HashMap<String, HashMap<String,String>>();
		
		Scanner scanner = new Scanner(System.in);
		

 		
		int menu	=	0;	// 메뉴값 초기화
		
		
			while(true) {
				
				
			System.out.println(" =================== ");
			System.out.println("다음 메뉴 중 하나를 선택하세요.");
			System.out.println(" =================== ");
			System.out.println(" 1. 회원 추가 하기");
			System.out.println(" 2. 회원 목록 보기");
			System.out.println(" 3. 회원 정보 수정 하기");
			System.out.println(" 4. 회원 정보 삭제 하기");
			System.out.println(" 5. 종료하기");
			
			menu = scanner.nextInt(); // 메뉴 선택 
			
			
			if(menu == 1) {
				
				HashMap<String, String> hashmap =	new HashMap<String, String>(); //hashmap에 이름 연락처 , 구분 등록

				System.out.println(" 등록할 회원의 정보를 입력하세요");
				System.out.print(" 이름 : ");
				String name		= scanner.next();
				hashmap.put("name",name);
				
				System.out.print(" 연락처 : ");
				String contact	=  scanner.next();
				hashmap.put("contact", contact );
				
				System.out.print(" 구분 (가족, 친구 , 회사 ,기타 등) : ");
				String part		=  scanner.next();
				hashmap.put("part", part);
				
				
				ALHM.put(contact, hashmap);					// 등록한 연락처의 키값을 contact value를 hashmap으로 alhm에 삽입
				
			}if(menu == 2) {
				
				Set<String> keys = ALHM.keySet(); // Set keys에 contact 데이터를 대입.

				Iterator<String> iterator = keys.iterator(); // keys에 있는 모든 값을 검색하겠다.
				System.out.println("총 " + ALHM.size() + "명의 회원이 저장되어 있습니다." );
				
				
				while(iterator.hasNext()) { // 이터레이터 안에 값이 있으면 출력 아니면 종료되게 조건 지정
					
	
					String key = iterator.next();
					HashMap<String, String> hm = ALHM.get(key);
					
					System.out.print("이름 : "	+ hm.get("name") + ", ");
					System.out.print("연락처 : "	+ hm.get("contact") + ", ");
					System.out.print("구분 : "	+ hm.get("part"));
					System.out.println();
				}	// 출력 후 처음으로 
			}	

			if(menu ==3) {
				
				Set<String> KeyUpdate = ALHM.keySet();
				Iterator<String> iteratorUpdate = KeyUpdate.iterator();
				
				System.out.println("수정할 회원의 이름을 입력하세요");
				String UpdateName = scanner.next();
				ArrayList<String> UpdateName1 = new ArrayList<String>();
				
				while(iteratorUpdate.hasNext()) {
					
					String updatekey = iteratorUpdate.next();
					HashMap<String, String> updatemap = ALHM.get(updatekey);
					
					if(updatemap.get("name").equals(UpdateName)) {
						
						UpdateName1.add(updatekey);
	
					
					}
				}
					System.out.println("총" + UpdateName1.size() + "명의 이름이 검색 되었습니다");
					System.out.println("아래 회원 목록중 수정 할 회원의 번호를 입력하세요.");
			
					for(int s = 0 ; s < UpdateName1.size(); s ++) {
						
						HashMap<String, String> updatehashmap = ALHM.get(UpdateName1.get(s));
						
						String updatehashmapname 	= updatehashmap.get("name");
						String updatehashmapcontact	= updatehashmap.get("contact");
						String updatehashmappart	= updatehashmap.get("part");
						
						System.out.print(s + 1 + ". 이름 :" + updatehashmapname + ",");
						System.out.print("연락처 :" + updatehashmapcontact + ",");
						System.out.println("구분 :" + updatehashmappart );
						
					}int d = scanner.nextInt();
					ALHM.remove(UpdateName1.get(d-1));

					HashMap<String, String> updhm =	new HashMap<String, String>(); 

					System.out.println(" 등록할 회원의 정보를 입력하세요");
					System.out.print(" 이름 : ");
					String name		= scanner.next();
					updhm.put("name",name);
					
					System.out.print(" 연락처 : ");
					String contact	=  scanner.next();
					updhm.put("contact", contact );
					
					System.out.print(" 구분 (가족, 친구 , 회사 ,기타 등) : ");
					String part		=  scanner.next();
					updhm.put("part", part);
					
					ALHM.put(contact, updhm);
					System.out.println("수정이 완료 되었습니다.");
					
			}
			if(menu ==4) {
				
				Set<String> keys2 = ALHM.keySet();
				Iterator<String> iterator2	=	keys2.iterator();
				
				
				System.out.println("삭제할 이름을 입력하세요.");
				String name = scanner.next();
				ArrayList<String> removename = new ArrayList<String>();
				
				while(iterator2.hasNext()) {
					
					String key2	=	iterator2.next();
					HashMap<String, String> hashmap2 = ALHM.get(key2);
			
					if(hashmap2.get("name").equals(name)) {
						

						removename.add(key2);
					
						}
					}
					if(removename.isEmpty()) {
						
						System.out.println("검색된 연락처가 없습니다.");
					}else {
					
						System.out.println("총 " + removename.size() + "명 입니다.");
						System.out.println("아래 목록중 삭제할 회원의 번호를 입력하세요.");
						
						for(int i = 0 ; i <removename.size(); i ++) {
		
							HashMap<String, String> one = ALHM.get(removename.get(i));
							String name1 	= one.get("name");
							String number	=one.get("contact");
							String part		=one.get("part");
							
							System.out.print(i +1 + ". 이름 = "  + name1 +", ");
							System.out.print("연락처 :" + number + ", " );
							System.out.println("구분 : " + part);
							
							
						}
						int j = scanner.nextInt();
						ALHM.remove(removename.get(j-1));
				
				
			}
				}
				
				
			if(menu >=5) {
				
				System.out.println("연락처 프로그램이 종료됩니다.");
				break;
			}
			}
			
			scanner.close();
}
			}
	
    ```
    
# Contact.java

```java

package lib;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.InputMismatchException;
import java.util.Scanner;
import java.util.Set;

public class Contact {
/* 전체 연락처 받을 HashMap 변수 선언 
 * [전체 연락처 HashMap(allContact)] 구조: 
 * 		key: 전화번호, value: 한명의 연락처 HashMap 
 * 		
 * 		[한명의 연락처 HashMap] 구조(key 고정): 
 * 			key: "nm", 		value: 이름 
 * 			key: "phoneno", value: 전화번호 
 * 			key: "clfc", 	value: 구분  		*/
	private HashMap<String, HashMap<String, String>> allContact = null;
	
//	Contact() 생성자: 전체 연락처 HashMap(allContact) 객체 생성
	public Contact() {
		this.allContact = 
				new HashMap<String, HashMap<String,String>>();
	}	

//	void printMenu(): 초기 메뉴 구성 화면 출력
	public void printMenu() {
		System.out.println("========================");
		System.out.println(" 다음 메뉴 중 하나를 선택하세요.");
		System.out.println("========================");
		System.out.println("1. 연락처 추가");
		System.out.println("2. 연락처 목록 보기");
		System.out.println("3. 연락처 정보 수정하기");
		System.out.println("4. 연락처 삭제");
		System.out.println("5. 종료");
		System.out.print("메뉴 번호 입력>> ");
	}
	
//	int isRightInteger(Scanner scanner):
//		scanner.nextInt() 유효성 검사
//		입력값이 올바를 경우 입력값을 정수로 반환, 입력값이 잘못됐을 경우 -1 반환
	public int isRightInteger(Scanner scanner) {
		try {
			return scanner.nextInt();
		} catch (InputMismatchException e) {
			scanner.nextLine();
			return -1;
		}
	}
	
//	HashMap<String, String> inputOneContactInfo(Scanner scanner):
//		이름, 전화번호, 구분을 입력받아 한명의 연락처 HashMap으로 반환
	public HashMap<String, String> inputOneContact(Scanner scanner) {
		HashMap<String, String> oneContact = new HashMap<String, String>();

		System.out.print("이름: ");
		oneContact.put("nm", scanner.next());		// 이름 입력				
		
		System.out.print("전화번호[ex) 01012345678]: ");
		oneContact.put("phoneno", scanner.next());	// 전화번호 입력				
		
		System.out.print("구분[ex) 1.가족, 2.친구, 3.회사, 4.기타]: ");
		String classification = scanner.next();	
		switch (classification) {					// 구분 조건부 입력
		case "1":
		case "가족":
			oneContact.put("clfc", "가족");
			break;
			
		case "2":
		case "친구":
			oneContact.put("clfc", "친구");
			break;
		
		case "3":
		case "회사":
			oneContact.put("clfc", "회사");
			break;
		
		case "4":
		case "기타":
			oneContact.put("clfc", "기타");
			break;
		
		default:
			oneContact.put("clfc", classification);;
			System.out.println(classification + " 구분에 추가 되었습니다.");
			break;
		}
		
		return oneContact;
	}
	
//	void printOneContact(String key): 
//		전화번호(key)로 전체 연락처 HashMap을 검색하여 해당 연락처 정보 화면에 출력
	public void printOneContact(String key) {
		HashMap<String, String> oneContact = 
								  this.allContact.get(key);
		
		System.out.println("이름: "			+ oneContact.get("nm")
						 + ", 전화번호: " 	+ oneContact.get("phoneno")
						 + ", 구분: "		+ oneContact.get("clfc"));
	}
	
	
//	ArrayList<String> getMatchKeysOfName(String name): 
//		이름값을 입력받아 전체 연락처 HashMap(allContact)에서 
//		같은 이름값을 가지는 key(전화번호)들을 ArrayList<String>에 저장하여 반환
	public ArrayList<String> getMatchKeysOfName(String name) {
		Set<String> keys 			= this.allContact.keySet();
		ArrayList<String> matchKeys = new ArrayList<String>();
		
		for(String key : keys) {
			HashMap<String, String> oneContact = 
									  this.allContact.get(key);
			
			if(oneContact.get("nm").equals(name)) {
				matchKeys.add(key);
			}
		}
		
		return matchKeys;
	}
	
//	boolean addContact(HashMap<String, String> oneContact): 
//		(menu 1)
//		입력받은 한명의 연락처 HashMap을 전체 연락처 HashMap(allContact)에 추가
//		중복 연락처 없으면 전체 연락처 HashMap에 추가하고 true 반환, 
//		중복 연락처 존재하면 추가 안하고 false 반환
	public boolean addContact(HashMap<String, String> oneContact) {
//		중복 연락처 유무 확인 -> 존재할 경우 중복 연락처 출력 후 false 반환후 메소드 종료
		if(this.allContact.containsKey(oneContact.get("phoneno"))) {
			System.out.println("다음의 중복된 연락처가 존재합니다.");
			this.printOneContact(oneContact.get("phoneno"));
			
			return false;
		}else {
			this.allContact.put(oneContact.get("phoneno"), oneContact);
			
			return true;
		}
	}
	
//	void printAllContact(): 
//		(menu 2)
//		전체 연락처 HashMap(allContact)에 있는 모든 연락처 출력
	public void printAllContact(){
		Set<String> keys = this.allContact.keySet();
		
		System.out.println("총 " + this.allContact.size()
						 + "명의 연락처가 저장되어 있습니다.");
		
		for(String key : keys) {
			this.printOneContact(key);
		}
	}
	
//	void modifyContact(Scanner scanner):
//		(menu3)
//		이름값을 입력받아 같은 이름값을 가지는 연락처들 출력후 선택을 입력받아 해당 연락처 수정
	public void modifyContact(Scanner scanner) {
		System.out.println("수정할 연락처의 이름을 입력하세요.");
		System.out.print("이름: ");
		String name = scanner.next();
		
		ArrayList<String> matchKeys = this.getMatchKeysOfName(name);
		
		if(matchKeys.isEmpty()) {
			System.out.println("해당하는 연락처 정보가 없습니다.");			
		}else {
			while(true) {
				System.out.println("총 " + matchKeys.size()
								 + "개의 목록이 검색되었습니다.");
				for(int i=0; i<matchKeys.size(); i++) {
					System.out.print((i+1) + ". ");
					this.printOneContact(matchKeys.get(i));			
				}
				
				System.out.print("목록 중 수정할 번호를 입력하세요(0: 취소)>> ");
				
				int num = this.isRightInteger(scanner) - 1;
				
				if(num == -1) {		//수정 종료
					break;
				}else if((num > matchKeys.size()-1) || (num < -1)) {
					System.out.println("입력값이 올바르지 않습니다.");
					System.out.println();
				}else {				//수정 실행
					System.out.println("수정할 정보를 입력하세요.");
					HashMap<String, String> inputContact = 
										this.inputOneContact(scanner);
					String modifyKey = matchKeys.get(num);
					HashMap<String, String> oneContact = 
										this.allContact.get(modifyKey);
											
								// 전화번호를 수정 안했을 경우
					if(modifyKey.equals(inputContact.get("phoneno"))) {
						oneContact.put("nm",   inputContact.get("nm"));
						oneContact.put("clfc", inputContact.get("clfc"));
						
						System.out.println("연락처 수정이 완료되었습니다.");
						break;
					}else {		// 전화번호를 수정 했을 경우
						if(this.addContact(inputContact)) {
							this.allContact.remove(matchKeys.get(num));
							System.out.println("연락처 수정이 완료되었습니다.");
							break;
						}else {		// 중복되는 번호 존재하여 연락처 수정 실패
							System.out.println("연락처 수정을 실패했습니다.");
							System.out.println();
						}
					}					
				}						
			}
		}
	}
	
//	void removeContact(Scanner scanner):
//		(menu 4)
//		이름값을 입력받아 같은 이름값을 가지는 연락처들 출력후 선택을 입력받아 해당 연락처 삭제
	public void removeContact(Scanner scanner) {
		System.out.println("수정할 연락처의 이름을 입력하세요.");
		System.out.print("이름: ");
		String name = scanner.next();
		
		ArrayList<String> matchKeys = this.getMatchKeysOfName(name);
				
		if(matchKeys.isEmpty()) {
			System.out.println("해당하는 연락처 정보가 없습니다.");			
		}else {			
			while(true) {
				System.out.println("총 " + matchKeys.size()
								 + "개의 목록이 검색되었습니다.");
				for(int i=0; i<matchKeys.size(); i++) {
					System.out.print((i+1) + ". ");
					this.printOneContact(matchKeys.get(i));			
				}
				
				System.out.print("목록 중 삭제할 번호를 입력하세요(0: 취소)>> ");
				int num = this.isRightInteger(scanner) - 1;
				
				if(num == -1) {		//삭제 종료
					break;
				}else if((num > matchKeys.size()-1) || (num < -1)) {
					System.out.println("입력값이 올바르지 않습니다.");
					System.out.println();
				}else {				//삭제 실행
					this.allContact.remove(matchKeys.get(num));				
					System.out.println("연락처 삭제가 완료되었습니다.");
					break;
				}				
			}
		}
	}
}

```

# ContactMain.java

```java

package main;

import java.util.HashMap;
import java.util.Scanner;

import lib.Contact;

public class ContactMain {

	public static void main(String[] args) {		
		Scanner scanner = new Scanner(System.in);
		Contact contact = new Contact();
		
		boolean flag = true;
		while(flag) {
			contact.printMenu();
			
			int menuNo = contact.isRightInteger(scanner);
			System.out.println();
			
			switch (menuNo) {
			case 1:		//연락처 추가
				System.out.println("등록할 연락처의 정보를 입력하세요.");
				HashMap<String, String> inputContact = 
								 contact.inputOneContact(scanner);
				
				if(contact.addContact(inputContact)) {
					System.out.println("연락처 추가가 완료되었습니다.");
				}else {		// 중복되는 번호 존재하여 연락처 추가 실패
					System.out.println("연락처 추가를 실패했습니다.");
				}
				break;
				
			case 2:		//연락처 목록 보기
				contact.printAllContact();
				break;
				
			case 3:		//연락처 정보 수정
				contact.modifyContact(scanner);
				break;
				
			case 4:		//연락처 삭제
				contact.removeContact(scanner);
				break;
				
			case 5:		//종료
				System.out.println("종료되었습니다.");
				flag = false;
				scanner.close();
				break;

			default:	//입력값이 올바르지 않을 경우
				System.out.println("입력 값이 올바르지 않습니다.(1-5 사이의 숫자 입력)");
				break;
			}
			
			System.out.println();
		}
		
	}

}

```

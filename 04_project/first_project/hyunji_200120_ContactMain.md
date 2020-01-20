# java

```java
package contact;

import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Contact contact = new Contact();
		Scanner scanner = new Scanner(System.in);
		boolean pause = true;
		while(pause) {			
			contact.mainMenu();
			String number = scanner.next();
			switch(number) {
				case "1":
					contact.add("등록");
					break;
				case "2":
					contact.list();
					break;
				case "3":
					contact.modify();
					break;
				case "4":
					contact.delete();
					break;
				case "5":
					System.out.println("종료되었습니다.");
					scanner.close();
					pause = false;
					break;
				default : 	
					System.out.println("유효하지 않은 입력입니다. 1부터 5까지의 숫자만 입력하세요.");
			}
		}
	}
}


```
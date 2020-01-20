# java 

```java
package contact;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Scanner;
import java.util.Set;

public class Contact {
	String name, cellphone, sort; 
	//전체 연락처를 담은 HashMap ---- total
	HashMap<String, HashMap<String,String>> total = new HashMap<String, HashMap<String, String>>();
	//한 사람의 HashMap ---- personal
	HashMap<String, String> personal = new HashMap<String, String>();
	Scanner scanner = new Scanner(System.in);

	public void mainMenu() {	
		//초기 화면의 메뉴를 출력한다.
		System.out.println(
				 "\n"+"=============================="
				+"\n"+ "  다음 메뉴의 번호 중 하나를  선택하세요." 
				+"\n"+ "=============================="
				+"\n"+ "1. 회원 추가"
				+"\n"+ "2. 회원 목록 보기"
				+"\n"+ "3. 회원 정보 수정하기"
				+"\n"+ "4. 회원 삭제"
				+"\n"+ "5. 종료"
				+"\n");
	}
	public void add(String createOrMod) {	
		//등록하거나 수정 시 연락처를 추가한다.
		personal = new HashMap<String, String>(); 			
		System.out.println("\n"+createOrMod+"할 회원의 정보를 입력하세요.");
		System.out.print("이름 : ");
		personal.put("이름", name = scanner.next());
		System.out.print("전화번호(ex. 01012345678) : ");				 
		personal.put("전화번호", cellphone = scanner.next());
		System.out.print("구분 (ex. 가족, 친구, 회사, 기타) : ");		
		personal.put("구분", sort = scanner.next());
		total.put(cellphone, personal);

	}
	public void list() {	
		//저장된 회원의 목록을 확인한다.
		System.out.println("총 " + total.size() + "명의 회원이 저장되어 있습니다.");
		Set<String> keys = total.keySet();
		Iterator<String> it = keys.iterator(); 
		while(it.hasNext()) {
				String key = it.next();
				System.out.println("회원정보 : 이름 = "+total.get(key).get("이름")
								  +", 전화번호 : " + key 
								  +", 구분 : " + total.get(key).get("구분"));
		}
	}
	public ArrayList<String> matchNameMembers() {	
		//입력값과 매치되는 이름이 연락처에 있을 경우에만 사용되는 메소드입니다.
		//입력값과 매치되는 이름이 연락처에 있을 시 ArrayList에 전화번호를 value값으로 추가한다. 
		String nameKey = scanner.next();
		ArrayList<String> matchNameMembers = new ArrayList<String>();
		for(String key : total.keySet()) {
			if(nameKey.equals(total.get(key).get("이름"))) {
				matchNameMembers.add(key);
			}
		}return matchNameMembers;
	}
	public void searchNModOrDel(ArrayList<String> matchNameMembers,String modOrDel) {
		//입력값과 매치되는 이름이 연락처에 있을 경우에만 사용되는 메소드입니다.
		//출력할 목록의 번호를 ArrayList의 index와 연결시켜보여주고
		//, ArrayList로부터 전화번호를 얻어 personal HashMap에 접근한다.
		System.out.print("\n"+"총 " 
				+ matchNameMembers.size()+"명의 회원이 검색되었습니다." 
				+"\n"+"아래 목록 중 "+modOrDel+"할 회원의 번호를 입력하세요"	//수정할건지 삭제할건지
				+"\n");
		for(int i = 0 ;i < matchNameMembers.size() ; i++) {
			System.out.println(i + 1
					+". " +"이름 = " + total.get(matchNameMembers.get(i)).get("이름")
					+", " + "전화번호 : " + matchNameMembers.get(i) 
					+", " + "구분 : " + total.get(matchNameMembers.get(i)).get("구분"));
		}
		//번호를 입력받아 번호에 해당하는 목록의 연락처 삭제
		int repeatedNum = scanner.nextInt();
		total.remove(matchNameMembers.get(repeatedNum-1));

	}

	public void modify() {
		System.out.print( "\n"+"수정할 회원의 이름을 입력하세요"
				 +"\n"+"이름 : ");
		//입력값과 매치되는 이름이 연락처에 있을 시 ArrayList에 전화번호를 value값으로 추가한다.
		ArrayList<String> matchNameMembers = this.matchNameMembers(); 
		if(matchNameMembers.isEmpty()){ //ArrayList에 요소가 없다는 것은 입력받은 이름과 매치되는 연락처가 없다는 것이다.
		System.out.println("해당하는 회원정보가 없습니다.");
		}
		else {	
			//ArrayList를 parameter로 받아 요소들을 보여주고 수정한다.
			this.searchNModOrDel(matchNameMembers, "수정"); 
			//번호를 입력받아 번호에 해당하는 목록의 연락처 삭제 후 새로운 연락처를 생성한다.
			this.add("수정"); //회원추가와 같은 메소드.
			System.out.println("수정이 완료되었습니다.");
		}
	}
	public void delete() { 
		System.out.print( "\n"+"삭제할 회원의 이름을 입력하세요"
				 +"\n"+"이름 : ");
		ArrayList<String> matchNameMembers = this.matchNameMembers();		
		//ArrayList를 parameter로 받아 요소들을 보여주고 삭제한다.
		if(matchNameMembers.isEmpty()){
				System.out.println("해당하는 회원정보가 없습니다.");
			}
		else {	//번호를 입력받아 번호에 해당하는 목록의 연락처 삭제
				this.searchNModOrDel(matchNameMembers, "삭제");
				System.out.println("삭제가 완료되었습니다.");
		}
	}
}


```


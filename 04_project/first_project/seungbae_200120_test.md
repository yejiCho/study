# java
``` java
package main;

 

import java.util.ArrayList;

import java.util.HashMap;

import java.util.InputMismatchException;

import java.util.Iterator;

import java.util.Scanner;

import java.util.Set;

 

public class Contact {

    static Scanner input = new Scanner(System.in);

    static HashMap<String, HashMap<String, String>> doublemap = new HashMap<String, HashMap<String, String>>();

    public static void main(String[] args) {

    	final int INSERT = 1;

    	final int ALLNUM = 2;

    	final int MODIFY = 3;

    	final int DELETE = 4;

    	final int EXIT = 5;

    	String name; String number; String relationship; 

    	Set<String>keys = doublemap.keySet();

    	Iterator<String> iterator = keys.iterator();

    	ArrayList<String> ArrayName;

    	

    	while(true) {

    	HashMap<String, String> map = new HashMap<String, String>();

    	System.out.println("\r==========================");

        System.out.println("    다음 메뉴 중 하나를 선택하세요. ");

        System.out.println("==========================");

        System.out.println("1. 회원 추가");

        System.out.println("2. 회원 목록 보기");

        System.out.println("3. 회원 정보 수정하기");

        System.out.println("4. 회원 삭제");

        System.out.println("5. 종료");

        int menu = input.nextInt();

        try {

        switch (menu) {

        case INSERT :

        	System.out.println("등록할 회원의 정보를 입력하세요.");

            System.out.println("이름: ");

            name = input.next();

            map.put("name", name);

            System.out.println("전화번호(ex: 01012345678): ");

            number = input.next();

            map.put("number", number);

            System.out.println("구분(ex.가족, 친구, 기타): ");

            relationship = input.next();

            map.put("relationship", relationship);

            doublemap.put(number, map);

        	break;

        	

        case ALLNUM :

        	System.out.println("총 " + doublemap.size() + " 명의 회원이 저장되어 있습니다." );

            keys = doublemap.keySet();

            iterator = keys.iterator();

            while(iterator.hasNext()) {

               number = iterator.next();

               map = doublemap.get(number);

               System.out.println("회원정보 : " 

               + "이름: " + map.get("name") + ", "  

               + "전화번호(ex: 01012345678): " + map.get("number") + ", " 

               + "구분(ex.가족, 친구, 기타): " + map.get("relationship"));

            }          

        	break;

        	

        case MODIFY :

        	 System.out.println("수정할 회원의 이름을 입력하세요.");

             System.out.println("이름 : ");

             name = input.next();

             ArrayName = new ArrayList<String>();

             keys = doublemap.keySet();

             iterator = keys.iterator();

             while(iterator.hasNext()) {

                number = iterator.next();

                map = doublemap.get(number);

                if(map.get("name").equals(name)){

                   ArrayName.add(number);   

                }               

             }if(ArrayName.isEmpty()) {

                System.out.println("해당하는 회원 정보가 없습니다.");

             }else {

                System.out.println("총 " + ArrayName.size() + " 개의 목록이 검색되었습니다.");

                System.out.println("아래 목록중 수정할 회원의 번호를 입력하세요.");

                for(int i = 0; i < ArrayName.size(); i++ ) {               

                   String newname = ArrayName.get(i);

                   map = doublemap.get(newname);

                   System.out.println((i + 1) +"." 

                   + "이름  : " + map.get("name") + ", "

                   + " 전화번호  : " + map.get("number") + ", "

                   + " 구분 : " + map.get("relationship"));

                }

                int newname = input.nextInt();

                doublemap.remove(ArrayName.get(newname-1));

                System.out.println("수정할 회원의 이름을 입력하세요.");

                System.out.print("이름 : ");

                name = input.next();

                map.put("name", name);

                System.out.print("전화번호 : ");

                number = input.next();

                map.put("number", number);

                System.out.print("구분 : ");

                relationship = input.next();

                map.put("relationship", relationship);

                doublemap.put(number, map);

                System.out.println("수정이 완료되었습니다.");

             }

        	break;

        	

        case DELETE:

        	System.out.println("삭제할 회원의 이름을 입력하세요.");

            System.out.println("이름 : ");

            name = input.next();

            ArrayName = new ArrayList<String>();

            keys = doublemap.keySet();

            iterator = keys.iterator();

            while(iterator.hasNext()) {

               number = iterator.next();

               map = doublemap.get(number);

               if(map.get("name").equals(name)) {

                  ArrayName.add(number);   

               }               

            }if(ArrayName.isEmpty()) {

               System.out.println("해당하는 회원 정보가 없습니다.");

            }else {

               System.out.println("총 " + ArrayName.size() + " 개의 목록이 검색되었습니다.");

               for(int i = 0; i < ArrayName.size(); i++ ) {               

                  String matchname = ArrayName.get(i);

                  map = doublemap.get(matchname);

                  System.out.println((i + 1) + "." 

                  + "이름  : " + map.get("name") + ", "

                  + " 전화번호  : " + map.get("number") + ", "  

                  + " 구분 : " + map.get("relationship"));

               }

               System.out.println("아래 목록 중 삭제할 회원의 번호를 입력하세요.");

               int delname = input.nextInt();

               doublemap.remove(ArrayName.get(delname-1));

               System.out.println("삭제가 완료되었습니다.");

            }

        	break;

        	

        case EXIT:

        	System.out.println("종료되었습니다.");

        	return;

        default:

        	System.out.println("1번 ~ 5번만 가능합니다.");

        	break;

        }

        } catch (InputMismatchException e) {

        	input = new Scanner(System.in);

        	System.out.println("잘못입력하셨습니다.");

		}

		}

    }

}

```
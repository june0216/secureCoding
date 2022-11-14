//서버에서 돌고 있는 코드이다. 
protected void doPost(HttpServletRequest request, HttpServletResponse response) {
 //웹 서버에서 돌고있는 프로그램이라는 것을 알 수 있다. (URL로 소통한다)
  // Validate input (omitted)
 
  String username = request.getParameter("username");
  char[] password = request.getParameter("password").toCharArray();
  boolean rememberMe = Boolean.valueOf(request.getParameter("rememberme"));
//remeberMe(기억하기 위해 체크박스) - true, false
   
  LoginService loginService = new LoginServiceImpl();
         
  if (rememberMe) {//체크했다고 가정한다. 
    if (request.getCookies()[0] != null && 
	    request.getCookies()[0].getValue() != null) {
//웹 브라우저에서 들어온 적이 있으면 쿠키 정보가세팅되어 있을 것이다. 
			
      String[] value = request.getCookies()[0].getValue().split(";");
//쿠키 정보에서 ; 이를 기준으로 문자열을 자른다. 
       
      if (!loginService.isUserValid(value[0], value[1].toCharArray())) {
//[0] = 유저 네임, [1]= 패스워드
        // Set error and return
      } else {
        // Forward to welcome page
      }
    } else {//쿠키가 없다면 
        boolean validated = loginService.isUserValid(username, password);
       //로그인을 한다. 
        if (validated) {
//해당 세션에 쿠키 세팅한다. 
          Cookie loginCookie = new Cookie("rememberme", username
                             + ";" + new String(password));
          response.addCookie(loginCookie);//쿠키에 세팅하라
//rememberme 쿠키는 서버에서 정의하기 나름이다 . 키와 벨류로 구분할 수 있다. (설계하기 나름이다)
//해당 서버가 세팅하는 것이다 -> 어떤 걸 써도 상관없다
          // ... Forward to welcome page
        } else {
          // Set error and return
        }
     }
   } else {
     // No remember-me functionality selected
     // Proceed with regular authentication;
     // if it fails set error and return
   }
     
  Arrays.fill(password, ' ');
}

//민감한 데이터의 수명을 제한해야 한다. 
//민감한 데이터를 사용 이후 꼭 공백이나 0으로 지워야 한다. 
class password{
  public static void main(String args[]) throws IOException{
    Console C = System.console();
    
    if(c == null)
    {
      System.exit(1);
    }
    String username = c.readLine("enter your name");
    char[] password = c.readLine("enter your password");
    boolean isValidUser = verify(username, password);
    Arrays.fill(password, " "); //민감한 데이터인 패스워드를 사용한 후 공백으로 지웠다. 
    
    if(isValidUser){
      throw new SecurityException("Invalid Credentials");
    }
  }
  
  private static final boolean verify(String name, char[] password)
  {
       //....
      return result;
  }

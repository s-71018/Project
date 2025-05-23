/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package dao;
import java.sql.*;

/**
 *
 * @author Shraddha
 */
public class ConnectionProvider {
    private static Connection con;
    
    public static Connection getCon(){
        try{
            if (con == null || con.isClosed()) {
            Class.forName("com.mysql.cj.jdbc.Driver");
            con = DriverManager.getConnection("jdbc:mysql://localhost:3306/cms?useSSL=false","root","root");
            return con;
            }
        }catch(Exception e){
            return null;
        }
        return con;
    }
    
}

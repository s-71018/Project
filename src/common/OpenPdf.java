/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package common;

import javax.swing.JOptionPane;
import java.io.File;

/**
 *
 * @author Shraddha
 */
public class OpenPdf {
    public static void openById(String id){
        try{
            if((new File("C:\\Users\\Shraddha\\Downloads\\itextpdf-5.5.13.4.jar"+id+".pdf")).exists()){
                Process p = Runtime.getRuntime().exec(
                        "rundll32 url.dll,FileProtocolHandler C:\\Users\\Shraddha\\Downloads\\itextpdf-5.5.13.4.jar"+id+".pdf");
            }
            else
                JOptionPane.showMessageDialog(null, "File Doesn't Exist");
                
        }
        catch(Exception e){
            JOptionPane.showMessageDialog(null, e);
        }
    }
    
}

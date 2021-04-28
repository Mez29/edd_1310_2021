/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Ico.fes.poo.modelo;

import java.util.ArrayList;
import javax.swing.table.AbstractTableModel;

/**
 *
 * @author mez29
 */
public class ModeloTablaJugadores extends AbstractTableModel{
        private ArrayList<Jugador> data;
public ModeloTablaJugadores(){
 }

public  ModeloTablaJugadores ( ArrayList <Jugador>  data ) {
        this.data = data;
    }

    @Override
    public int getRowCount() {
        return data.size();
    }

    @Override
    public int getColumnCount() {
        return 8;
    }
 @Override
    public  String  getColumnName ( int  columnIndex ) {
        String columnName = " " ;
        switch (columnIndex) {
            case 0 :
                    columnName =  " Nombre " ;
                break ;
            case  1 :
                    columnName =  " Apellido Paterno " ;
                break ;
            case  2 :
                    columnName =  " Apellido Materno " ;
                break ;
            case  3 :
                    columnName =  " Apodo " ;
                break ;
            case  4 :
                    columnName =  " Equipo " ;
                break ;
            case  5 :
                    columnName =  " Pais " ;
                break ;
            case  6 :
                    columnName =  " Posicion " ;
                break;
            case  7 :
                    columnName =  " Numero " ;
                break ;

            default :
                columnName = " ND " ;
        }
        return columnName;
    }

    @Override
    public  Class <?>  getColumnClass ( int  columnIndex ) {
        switch (columnIndex) {
            case  0 :
                return String.class;
            case  1 :
                return String.class;
            case  2 :
                return String.class;
            case  3 :
                return  String.class;
            case  4 :
                return  String.class;
            case  5  :
                return String.class;
            case  6 :
                return String.class;
            case  7 :
                return Integer.class;
            default :
                return String.class; 
        }
    }
    @Override
    public  boolean  isCellEditable ( int  rowIndex , int  columnIndex ) {
        return  true ;
    }

    @Override
    public Object getValueAt ( int  rowIndex , int  columnIndex ) {
        Jugador tmp = data. get(rowIndex);
        switch (columnIndex) {
            case 0 :
                return tmp . getNombre();
            case  1 :
                return tmp . getApellidoPaterno();
            case  2 :
                return tmp . getApellidoMaterno();
            case  3 :
                return tmp . getApodo();
            case  4 :
                return tmp . getEquipo();
            case  5 :
                return tmp . getPais();
            case  6 :
                return tmp . getPosicion(); 
            case  7 :
                return tmp . getNumero();
            default :
                return  null ;
        }
    }

    @Override
    public  void  setValueAt ( Object  aValue , int  rowIndex , int  columnIndex ) {
        Jugador tmp= data.get(rowIndex);
        switch (columnIndex){
            case 0:
                tmp.setNombre((String)aValue);
                break;
            case 1:
                tmp.setApellidoPaterno((String)aValue);
                break;
            case 2:
                tmp.setApellidoMaterno((String)aValue);
                break;
            case 3:
                tmp.setApodo((String)aValue);
                break;
             case 4:
                tmp.setEquipo((String)aValue);
                break;
            case 5:
                tmp.setPais((String)aValue);
                break;
            case 6:
                tmp.setPosicion((String)aValue);
                break;
            case 7:
                tmp.setNumero((int)aValue);
            default:
                 throw new AssertionError();
        }
        data.set(rowIndex,tmp);
        this.fireTableCellUpdated(rowIndex, columnIndex);
    }
    
    public void agregarJugador(Jugador c) {
        data.add(c);
        this.fireTableDataChanged();
    } 
}
   
package cannata;

import java.util.*;
import java.util.stream.Collector;

public class ListComprehension {
    public static void main(String[] args) {
        ArrayList<List<Object>> emp = new ArrayList<List<Object>>(Arrays.asList(
                Arrays.asList(1, "MARTIN", "CARMEN", "MARTINCU", "3-MAR-90", "", "PRESIDENT", 4500, 0, 50, 0),
                Arrays.asList(10, "JACKSON", "MARTA", "JACKSOMT", "27-FEB-91", "", "WAREHOUSE MANAGER", 1507, 0, 45, 2),
                Arrays.asList(11, "HENDERSON", "COLIN", "HENDERCS", "14-MAY-90", "", "SALES REPRESENTATIVE", 1400, 10, 31, 3),
                Arrays.asList(12, "GILSON", "SAM", "GILSONSJ", "18-JAN-92", "", "SALES REPRESENTATIVE", 1490, 12.5, 32, 3),
                Arrays.asList(13, "SANDERS", "JASON", "SANDERJK", "18-FEB-91", "", "SALES REPRESENTATIVE", 1515, 10, 33, 3),
                Arrays.asList(14, "DAMERON", "ANDRE", "DAMEROAP", "9-OCT-91", "", "SALES REPRESENTATIVE", 1450, 17.5, 35, 3),
                Arrays.asList(15, "HARDWICK", "ELAINE", "HARDWIEM", "7-FEB-92", "", "STOCK CLERK", 1400, 0, 41, 6),
                Arrays.asList(16, "BROWN", "GEORGE", "BROWNGW", "8-MAR-90", "", "STOCK CLERK", 940, 0, 41, 6),
                Arrays.asList(17, "WASHINGTON", "THOMAS", "WASHINTL", "9-FEB-91", "", "STOCK CLERK", 1200, 0, 42, 7),
                Arrays.asList(18, "PATTERSON", "DONALD", "PATTERDV", "6-AUG-91", "", "STOCK CLERK", 795, 0, 42, 7),
                Arrays.asList(19, "BELL", "ALEXANDER", "BELLAG", "26-MAY-91", "", "STOCK CLERK", 850, 0, 43, 8),
                Arrays.asList(2, "SMITH", "DORIS", "SMITHDJ", "8-MAR-90", "", "VP, OPERATIONS", 2450, 0, 41, 1),
                Arrays.asList(20, "GANTOS", "EDDIE", "GANTOSEJ", "30-NOV-90", "", "STOCK CLERK", 800, 0, 44, 9),
                Arrays.asList(21, "STEPHENSON", "BLAINE", "STEPHEBS", "17-MAR-91", "", "STOCK CLERK", 860, 0, 45, 10),
                Arrays.asList(22, "CHESTER", "EDDIE", "CHESTEEK", "30-NOV-90", "", "STOCK CLERK", 800, 0, 44, 9),
                Arrays.asList(23, "PEARL", "ROGER", "PEARLRG", "17-OCT-90", "", "STOCK CLERK", 795, 0, 34, 9),
                Arrays.asList(24, "DANCER", "BONNIE", "DANCERBW", "17-MAR-91", "", "STOCK CLERK", 860, 0, 45, 7),
                Arrays.asList(25, "SCHMITT", "SANDRA", "SCHMITSS", "9-MAY-91", "", "STOCK CLERK", 1100, 0, 45, 8),
                Arrays.asList(3, "NORTON", "MICHAEL", "NORTONMA", "17-JUN-91", "", "VP, SALES", 2400, 0, 31, 1),
                Arrays.asList(4, "QUENTIN", "MARK", "QUENTIML", "7-APR-90", "", "VP, FINANCE", 2450, 0, 10, 1),
                Arrays.asList(5, "ROPER", "JOSEPH", "ROPERJM", "4-MAR-90", "", "VP, ADMINISTRATION", 2550, 0, 50, 1),
                Arrays.asList(6, "BROWN", "MOLLY", "BROWNMR", "18-JAN-91", "", "WAREHOUSE MANAGER", 1600, 0, 41, 2),
                Arrays.asList(7, "HAWKINS", "ROBERTA", "HAWKINRT", "14-MAY-90", "", "WAREHOUSE MANAGER", 1650, 0, 42, 2),
                Arrays.asList(8, "BURNS", "BEN", "BURNSBA", "7-APR-90", "", "WAREHOUSE MANAGER", 1500, 0, 43, 2),
                Arrays.asList(9, "CATSKILL", "ANTOINETTE", "CATSKIAW", "9-FEB-92", "", "WAREHOUSE MANAGER", 1700, 0, 44, 2)));

        System.out.println("select first_name, last_name from s_emp");
        emp.stream().forEach(e -> {
            System.out.println(e.get(2) + " " + e.get(1));
        });
        System.out.println();

        System.out.println("select first_name, last_name from s_emp where salary > 1500 and dept_id > 40");
        emp.stream().filter(e -> (Integer.parseInt(e.get(7).toString()) > 1500) && (Integer.parseInt(e.get(9).toString())) > 40).forEach(e -> {
            System.out.println(e.get(2) + " " + e.get(1));
        });
        System.out.println();

        System.out.println("select * from s_emp cross join s_emp");
        emp.stream().flatMap(v1 -> emp.stream().map(v2 -> Arrays.asList(v1, v2))).forEach(e -> System.out.println(e));

        System.out.println();

        System.out.println("select e.first_name, e.last_name, a.first_name, a.last_name from s_emp e inner join s_emp a on e.manager_id = a.id");
        emp.stream().flatMap(v1 -> emp.stream().map(v2 -> Arrays.asList (v1, v2))).filter(li -> li.get(0).get(10) == li.get(1).get(0))
                .forEach(e -> System.out.println(e.get(0).get(2) + " " + e.get(0).get(1) + " " + e.get(1).get(2) + " " + e.get(1).get(1)));
        System.out.println();

        System.out.println("select e_first name, e.last_name, e_salary, a.first_name, a.last_name, a_salary from s_emp e inner join s_emp a on e.manager_id = a.id where a.salary > 2*e.salary");

        emp.stream().flatMap(v1 -> emp.stream().map(v2 -> Arrays.asList (v1, v2))).filter(li -> li.get(0).get(10) == li.get(1).get(0) &&
                Integer.parseInt(li.get(1).get(7).toString()) > 2 * Integer.parseInt(li.get(0).get(7).toString()))
                .forEach(e -> System.out.println(e.get(0).get(2) + " " + e.get(0).get(1) + " " + e.get(0).get(7) + " " + e.get(1).get(2) + " " + e.get(1).get(1) + " " + e.get(1).get(7)));
        System.out.println();

    }
}

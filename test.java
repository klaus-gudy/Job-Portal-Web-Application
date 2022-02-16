// write a program that asks the users how many student grades they want to enter. The program should then use a loop to ask the user to enter student name and the student grade.program must save the student names and grades in a text file,with 1 student on each line. program should use loops and files to achieve the task.
class StudentGrades{
    public static void main(String[] args){
        int numberOfStudents = getNumberOfStudents();
        String fileName = "studentGrades.txt";
        try{
            FileWriter fileWriter = new FileWriter(fileName);
            BufferedWriter bufferedWriter = new BufferedWriter(fileWriter);
            for(int i = 0; i < numberOfStudents; i++){
                String studentName = getStudentName();
                int studentGrade = getStudentGrade();
                bufferedWriter.write(studentName + " " + studentGrade + "\n");
            }
            bufferedWriter.close();
            
}
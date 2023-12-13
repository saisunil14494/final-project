<!-- views/index.tpl -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>School Database</title>
</head>
<body>
    <h1>Classes</h1>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Class Name</th>
            <th>Actions</th>
        </tr>
        % for class_id, class_name in classes:
            <tr>
                <td>{{class_id}}</td>
                <td>{{class_name}}</td>
                <td>
                    <a href="/editClass/{{class_id}}">Edit</a>
                    <a href="/deleteClass/{{class_id}}">Delete</a>
                </td>
            </tr>
        % end
    </table>

    <h1>Students</h1>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Student Name</th>
            <th>Class ID</th>
            <th>Actions</th>
        </tr>
        % for student_id, student_name, class_id in students:
            <tr>
                <td>{{student_id}}</td>
                <td>{{student_name}}</td>
                <td>{{class_id}}</td>
                <td>
                    <a href="/editStudent/{{student_id}}">Edit</a>
                    <a href="/deleteStudent/{{student_id}}">Delete</a>
                </td>
            </tr>
        % end
    </table>

    <h2>Add Class</h2>
    <form action="/addClass" method="post">
        Class Name: <input type="text" name="class_name" required>
        <input type="submit" value="Add Class">
    </form>

    <h2>Add Student</h2>
    <form action="/addStudent" method="post">
        Student Name: <input type="text" name="student_name" required>
        Class ID: <input type="text" name="class_id" required>
        <input type="submit" value="Add Student">
    </form>
</body>
</html>
 
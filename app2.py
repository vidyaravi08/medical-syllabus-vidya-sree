import 'package:flutter/material.dart';

void main() {
  runApp(StudyApp());
}

class StudyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Medical Study App',
      theme: ThemeData(primarySwatch: Colors.blue),
      home: SubjectListPage(),
    );
  }
}

class SubjectListPage extends StatelessWidget {
  final List<String> subjects = [
    'Anatomy',
    'Physiology',
    'Biochemistry',
    'Pathology',
    'Pharmacology',
    'Microbiology',
    'Medicine',
    'Surgery',
    'Pediatrics',
    'OBG',
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Subjects')),
      body: ListView.builder(
        itemCount: subjects.length,
        itemBuilder: (context, index) {
          return ListTile(
            title: Text(subjects[index]),
            trailing: Icon(Icons.arrow_forward),
            onTap: () {
              Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) => LessonPage(subject: subjects[index]),
                ),
              );
            },
          );
        },
      ),
    );
  }
}

class LessonPage extends StatelessWidget {
  final String subject;

  LessonPage({required this.subject});

  final Map<String, List<String>> lessons = {
    'Anatomy': ['Bones of Skull', 'Muscles of Arm', 'Heart Anatomy'],
    'Physiology': ['Blood Circulation', 'Respiration', 'Nervous System'],
    'Biochemistry': ['Carbohydrate Metabolism', 'Proteins', 'DNA Structure'],
    'Pathology': ['Cell Injury', 'Inflammation', 'Neoplasia'],
    'Pharmacology': ['General Pharmacology', 'Antibiotics', 'Cardiac Drugs'],
    'Microbiology': ['Bacteria', 'Viruses', 'Immunology'],
    'Medicine': ['Diabetes Mellitus', 'Hypertension', 'Asthma'],
    'Surgery': ['Appendicitis', 'Hernia', 'Gallstones'],
    'Pediatrics': ['Growth Milestones', 'Vaccination', 'Common Childhood Illness'],
    'OBG': ['Pregnancy', 'Labor', 'Gynecological Disorders'],
  };

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(subject)),
      body: ListView.builder(
        itemCount: lessons[subject]?.length ?? 0,
        itemBuilder: (context, index) {
          return Card(
            child: ListTile(
              title: Text(lessons[subject]![index]),
              onTap: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) => LessonDetailPage(
                      lesson: lessons[subject]![index],
                    ),
                  ),
                );
              },
            ),
          );
        },
      ),
    );
  }
}

class LessonDetailPage extends StatelessWidget {
  final String lesson;

  LessonDetailPage({required this.lesson});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(lesson)),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Text(
          'Content for $lesson goes here.\n\n'
          'You can add notes, diagrams, or quizzes here.',
          style: TextStyle(fontSize: 18),
        ),
      ),
    );
  }
}

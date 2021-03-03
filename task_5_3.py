tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А'#, '10Б', '9А'
]

tutor_klass_gen = ((tutor, klass) for tutor, klass in zip(tutors, klasses))
print(next(tutor_klass_gen))
print(next(tutor_klass_gen))
print(next(tutor_klass_gen))
print(next(tutor_klass_gen))
print(next(tutor_klass_gen))
print(next(tutor_klass_gen))
print(next(tutor_klass_gen))
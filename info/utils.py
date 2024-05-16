import matplotlib.pyplot as plt

from info.models import Project


def draw_plan(project):
	fig, ax = plt.subplots()

	# Рисуем стены
	for wall in ['A', 'B', 'C', 'D']:
		wall_length = getattr(project, f'width_{wall.lower()}')
		if wall_length:
			ax.plot([0, wall_length], [0, 0], label=f'Стена {wall}', linestyle='-', marker='o')

	# Рисуем потолок
	ceiling_length = max([getattr(project, f'width_{wall.lower()}') for wall in ['A', 'B', 'C', 'D'] if
						  getattr(project, f'width_{wall.lower()}')])
	ax.plot([0, ceiling_length], [2, 2], label='Потолок', linestyle='-', marker='o')

	ax.set_aspect('equal')
	ax.legend()
	ax.set_title('Планировка проекта')
	ax.set_xlabel('Длина, м')
	ax.set_ylabel('Высота, м')

	plt.show()


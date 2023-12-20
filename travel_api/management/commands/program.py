from django.core.management.base import BaseCommand
from travel_api.models import *


# tour 5
program_5 = [
    {
        "tour": 5,
        "tour_days": 2,
        "tour_option": 3,
        "order": 1
    },
    {
        "tour": 5,
        "tour_days": 2,
        "tour_option": 4,
        "order": 2
    },
    {
        "tour": 5,
        "tour_days": 2,
        "tour_option": 5,
        "order": 3
    },
    {
        "tour": 5,
        "tour_days": 2,
        "tour_option": 36,
        "order": 4
    },
    {
        "tour": 5,
        "tour_days": 2,
        "tour_option": 37,
        "order": 5
    },
    {
        "tour": 5,
        "tour_days": 2,
        "tour_option": 19,
        "order": 6
    },
    {
        "tour": 5,
        "tour_days": 2,
        "tour_option": 38,
        "order": 7
    },
    {
        "tour": 5,
        "tour_days": 2,
        "tour_option": 22,
        "order": 8
    },
    {
        "tour": 5,
        "tour_days": 3,
        "tour_option": 4,
        "order": 1
    },
    {
        "tour": 5,
        "tour_days": 3,
        "tour_option": 10,
        "order": 2
    },
    {
        "tour": 5,
        "tour_days": 3,
        "tour_option": 24,
        "order": 3
    },
    {
        "tour": 5,
        "tour_days": 3,
        "tour_option": 25,
        "order": 4
    },
    {
        "tour": 5,
        "tour_days": 3,
        "tour_option": 12,
        "order": 5
    },
    {
        "tour": 5,
        "tour_days": 3,
        "tour_option": 38,
        "order": 6
    },
    {
        "tour": 5,
        "tour_days": 3,
        "tour_option": 39,
        "order": 7
    },
    {
        "tour": 5,
        "tour_days": 3,
        "tour_option": 22,
        "order": 8
    },
{
        "tour": 5,
        "tour_days": 4,
        "tour_option": 4,
        "order": 1
    },
    {
        "tour": 5,
        "tour_days": 4,
        "tour_option": 40,
        "order": 2
    },
    {
        "tour": 5,
        "tour_days": 4,
        "tour_option": 41,
        "order": 3
    },
    {
        "tour": 5,
        "tour_days": 4,
        "tour_option": 19,
        "order": 4
    },
    {
        "tour": 5,
        "tour_days": 4,
        "tour_option": 38,
        "order": 5
    },
    {
        "tour": 5,
        "tour_days": 4,
        "tour_option": 22,
        "order": 6
    },
    {
        "tour": 5,
        "tour_days": 5,
        "tour_option": 14,
        "order": 1
    },
    {
        "tour": 5,
        "tour_days": 5,
        "tour_option": 4,
        "order": 2
    },
    {
        "tour": 5,
        "tour_days": 5,
        "tour_option": 42,
        "order": 3
    },
    {
        "tour": 5,
        "tour_days": 5,
        "tour_option": 43,
        "order": 4
    },
    {
        "tour": 5,
        "tour_days": 5,
        "tour_option": 18,
        "order": 5
    }
]

# tour 6
program_6 = [
    {
        "tour": 6,
        "tour_days": 2,
        "tour_option": 3,
        "order": 1
    },
    {
        "tour": 6,
        "tour_days": 2,
        "tour_option": 4,
        "order": 2
    },
    {
        "tour": 6,
        "tour_days": 2,
        "tour_option": 5,
        "order": 3
    },
    {
        "tour": 6,
        "tour_days": 2,
        "tour_option": 19,
        "order": 4
    },
    {
        "tour": 6,
        "tour_days": 2,
        "tour_option": 44,
        "order": 5
    },
    {
        "tour": 6,
        "tour_days": 2,
        "tour_option": 45,
        "order": 6
    },
    {
        "tour": 6,
        "tour_days": 2,
        "tour_option": 46,
        "order": 7
    },
    {
        "tour": 6,
        "tour_days": 2,
        "tour_option": 47,
        "order": 8
    },
    {
        "tour": 6,
        "tour_days": 2,
        "tour_option": 22,
        "order": 9
    },
    {
        "tour": 6,
        "tour_days": 2,
        "tour_option": 13,
        "order": 10
    },
    {
        "tour": 6,
        "tour_days": 3,
        "tour_option": 4,
        "order": 1
    },
    {
        "tour": 6,
        "tour_days": 3,
        "tour_option": 48,
        "order": 2
    },
    {
        "tour": 6,
        "tour_days": 3,
        "tour_option": 27,
        "order": 3
    },
    {
        "tour": 6,
        "tour_days": 3,
        "tour_option": 20,
        "order": 4
    },
    {
        "tour": 6,
        "tour_days": 3,
        "tour_option": 8,
        "order": 5
    },
    {
        "tour": 6,
        "tour_days": 3,
        "tour_option": 22,
        "order": 6
    },
    {
        "tour": 6,
        "tour_days": 4,
        "tour_option": 4,
        "order": 1
    },
    {
        "tour": 6,
        "tour_days": 4,
        "tour_option": 49,
        "order": 2
    },
    {
        "tour": 6,
        "tour_days": 4,
        "tour_option": 50,
        "order": 3
    },
    {
        "tour": 6,
        "tour_days": 4,
        "tour_option": 46,
        "order": 4
    },
    {
        "tour": 6,
        "tour_days": 4,
        "tour_option": 51,
        "order": 5
    },
    {
        "tour": 6,
        "tour_days": 4,
        "tour_option": 21,
        "order": 6
    },
    {
        "tour": 6,
        "tour_days": 4,
        "tour_option": 8,
        "order": 7
    },
    {
        "tour": 6,
        "tour_days": 5,
        "tour_option": 14,
        "order": 1
    },
    {
        "tour": 6,
        "tour_days": 5,
        "tour_option": 4,
        "order": 2
    },
    {
        "tour": 6,
        "tour_days": 5,
        "tour_option": 52,
        "order": 3
    },
    {
        "tour": 6,
        "tour_days": 5,
        "tour_option": 17,
        "order": 4
    },
    {
        "tour": 6,
        "tour_days": 5,
        "tour_option": 18,
        "order": 5
    }
]

# tour 7
program_7 = [
    {
        "tour": 7,
        "tour_days": 2,
        "tour_option": 3,
        "order": 1
    },
    {
        "tour": 7,
        "tour_days": 2,
        "tour_option": 4,
        "order": 2
    },
    {
        "tour": 7,
        "tour_days": 2,
        "tour_option": 19,
        "order": 3
    },
    {
        "tour": 7,
        "tour_days": 2,
        "tour_option": 53,
        "order": 4
    },
    {
        "tour": 7,
        "tour_days": 2,
        "tour_option": 38,
        "order": 5
    },
    {
        "tour": 7,
        "tour_days": 2,
        "tour_option": 22,
        "order": 6
    },
    {
        "tour": 7,
        "tour_days": 3,
        "tour_option": 4,
        "order": 1
    },
    {
        "tour": 7,
        "tour_days": 3,
        "tour_option": 54,
        "order": 2
    },
    {
        "tour": 7,
        "tour_days": 3,
        "tour_option": 24,
        "order": 3
    },
    {
        "tour": 7,
        "tour_days": 3,
        "tour_option": 13,
        "order": 4
    },
    {
        "tour": 7,
        "tour_days": 3,
        "tour_option": 8,
        "order": 5
    },
    {
        "tour": 7,
        "tour_days": 3,
        "tour_option": 22,
        "order": 6
    },
    {
        "tour": 7,
        "tour_days": 4,
        "tour_option": 4,
        "order": 1
    },
    {
        "tour": 7,
        "tour_days": 4,
        "tour_option": 15,
        "order": 2
    },
    {
        "tour": 7,
        "tour_days": 4,
        "tour_option": 27,
        "order": 3
    },
    {
        "tour": 7,
        "tour_days": 4,
        "tour_option": 21,
        "order": 4
    },
    {
        "tour": 7,
        "tour_days": 4,
        "tour_option": 20,
        "order": 5
    },
    {
        "tour": 7,
        "tour_days": 4,
        "tour_option": 8,
        "order": 6
    },
    {
        "tour": 7,
        "tour_days": 4,
        "tour_option": 22,
        "order": 7
    },
    {
        "tour": 7,
        "tour_days": 5,
        "tour_option": 14,
        "order": 1
    },
    {
        "tour": 7,
        "tour_days": 5,
        "tour_option": 4,
        "order": 2
    },
    {
        "tour": 7,
        "tour_days": 5,
        "tour_option": 52,
        "order": 3
    },
    {
        "tour": 7,
        "tour_days": 5,
        "tour_option": 39,
        "order": 4
    },
    {
        "tour": 7,
        "tour_days": 5,
        "tour_option": 16,
        "order": 5
    },
    {
        "tour": 7,
        "tour_days": 5,
        "tour_option": 8,
        "order": 6
    },
    {
        "tour": 7,
        "tour_days": 5,
        "tour_option": 22,
        "order": 7
    },
    {
        "tour": 7,
        "tour_days": 6,
        "tour_option": 14,
        "order": 1
    },
    {
        "tour": 7,
        "tour_days": 6,
        "tour_option": 4,
        "order": 2
    },
    {
        "tour": 7,
        "tour_days": 6,
        "tour_option": 55,
        "order": 3
    },
    {
        "tour": 7,
        "tour_days": 6,
        "tour_option": 56,
        "order": 4
    },
    {
        "tour": 7,
        "tour_days": 6,
        "tour_option": 57,
        "order": 5
    },
    {
        "tour": 7,
        "tour_days": 6,
        "tour_option": 18,
        "order": 6
    }
]

# tour 8
program_8 = [
    {
        "tour": 8,
        "tour_days": 2,
        "tour_option": 3,
        "order": 1
    },
    {
        "tour": 8,
        "tour_days": 2,
        "tour_option": 35,
        "order": 2
    },
    {
        "tour": 8,
        "tour_days": 2,
        "tour_option": 52,
        "order": 3
    },
    {
        "tour": 8,
        "tour_days": 2,
        "tour_option": 59,
        "order": 4
    },
    {
        "tour": 8,
        "tour_days": 2,
        "tour_option": 60,
        "order": 5
    },
    {
        "tour": 8,
        "tour_days": 3,
        "tour_option": 4,
        "order": 1
    },
    {
        "tour": 8,
        "tour_days": 3,
        "tour_option": 61,
        "order": 2
    },
    {
        "tour": 8,
        "tour_days": 3,
        "tour_option": 62,
        "order": 3
    },
    {
        "tour": 8,
        "tour_days": 3,
        "tour_option": 18,
        "order": 4
    }
]

# tour 3
program_3 = [
    {
        "tour": 3,
        "tour_days": 2,
        "tour_option": 3,
        "order": 1
    },
    {
        "tour": 3,
        "tour_days": 2,
        "tour_option": 4,
        "order": 2
    },
    {
        "tour": 3,
        "tour_days": 2,
        "tour_option": 5,
        "order": 3
    },
    {
        "tour": 3,
        "tour_days": 2,
        "tour_option": 19,
        "order": 4
    },
    {
        "tour": 3,
        "tour_days": 2,
        "tour_option": 20,
        "order": 5
    },
    {
        "tour": 3,
        "tour_days": 2,
        "tour_option": 21,
        "order": 6
    },
    {
        "tour": 3,
        "tour_days": 2,
        "tour_option": 38,
        "order": 7
    },
    {
        "tour": 3,
        "tour_days": 2,
        "tour_option": 22,
        "order": 8
    },
    {
        "tour": 3,
        "tour_days": 3,
        "tour_option": 4,
        "order": 1
    },
    {
        "tour": 3,
        "tour_days": 3,
        "tour_option": 23,
        "order": 2
    },
    {
        "tour": 3,
        "tour_days": 3,
        "tour_option": 24,
        "order": 3
    },
    {
        "tour": 3,
        "tour_days": 3,
        "tour_option": 25,
        "order": 4
    },
    {
        "tour": 3,
        "tour_days": 3,
        "tour_option": 8,
        "order": 5
    },
    {
        "tour": 3,
        "tour_days": 3,
        "tour_option": 22,
        "order": 6
    },
    {
        "tour": 3,
        "tour_days": 4,
        "tour_option": 14,
        "order": 1
    },
    {
        "tour": 3,
        "tour_days": 4,
        "tour_option": 4,
        "order": 2
    },
    {
        "tour": 3,
        "tour_days": 4,
        "tour_option": 26,
        "order": 3
    },
    {
        "tour": 3,
        "tour_days": 4,
        "tour_option": 27,
        "order": 4
    },
    {
        "tour": 3,
        "tour_days": 4,
        "tour_option": 28,
        "order": 5
    },
    {
        "tour": 3,
        "tour_days": 4,
        "tour_option": 18,
        "order": 6
    }
]

# tour 4
program_4 = [
    {
        "tour": 4,
        "tour_days": 2,
        "tour_option": 4,
        "order": 1
    },
    {
        "tour": 4,
        "tour_days": 2,
        "tour_option": 5,
        "order": 2
    },
    {
        "tour": 4,
        "tour_days": 2,
        "tour_option": 29,
        "order": 3
    },
    {
        "tour": 4,
        "tour_days": 2,
        "tour_option": 30,
        "order": 4
    },
    {
        "tour": 4,
        "tour_days": 2,
        "tour_option": 38,
        "order": 5
    },
    {
        "tour": 4,
        "tour_days": 3,
        "tour_option": 4,
        "order": 1
    },
    {
        "tour": 4,
        "tour_days": 3,
        "tour_option": 31,
        "order": 2
    },
    {
        "tour": 4,
        "tour_days": 3,
        "tour_option": 27,
        "order": 3
    },
    {
        "tour": 4,
        "tour_days": 3,
        "tour_option": 32,
        "order": 4
    },
    {
        "tour": 4,
        "tour_days": 4,
        "tour_option": 14,
        "order": 1
    },
    {
        "tour": 4,
        "tour_days": 4,
        "tour_option": 4,
        "order": 2
    },
    {
        "tour": 4,
        "tour_days": 4,
        "tour_option": 33,
        "order": 3
    },
    {
        "tour": 4,
        "tour_days": 4,
        "tour_option": 34,
        "order": 4
    },
    {
        "tour": 4,
        "tour_days": 4,
        "tour_option": 35,
        "order": 5
    },
    {
        "tour": 4,
        "tour_days": 4,
        "tour_option": 18,
        "order": 6
    }
]

# tour 2
program = [
    {
        "tour": 2,
        "tour_days": 2,
        "tour_option": 3,
        "order": 1
    },
    {
        "tour": 2,
        "tour_days": 2,
        "tour_option": 4,
        "order": 2
    },
    {
        "tour": 2,
        "tour_days": 2,
        "tour_option": 5,
        "order": 3
    },
    {
        "tour": 2,
        "tour_days": 2,
        "tour_option": 6,
        "order": 4
    },
    {
        "tour": 2,
        "tour_days": 2,
        "tour_option": 7,
        "order": 5
    },
    {
        "tour": 2,
        "tour_days": 2,
        "tour_option": 8,
        "order": 6
    },
    {
        "tour": 2,
        "tour_days": 2,
        "tour_option": 9,
        "order": 7
    },
    {
        "tour": 2,
        "tour_days": 3,
        "tour_option": 4,
        "order": 1
    },
    {
        "tour": 2,
        "tour_days": 3,
        "tour_option": 10,
        "order": 2
    },
    {
        "tour": 2,
        "tour_days": 3,
        "tour_option": 11,
        "order": 3
    },
    {
        "tour": 2,
        "tour_days": 3,
        "tour_option": 12,
        "order": 4
    },
    {
        "tour": 2,
        "tour_days": 3,
        "tour_option": 13,
        "order": 5
    },
    {
        "tour": 2,
        "tour_days": 3,
        "tour_option": 22,
        "order": 6
    },
    {
        "tour": 2,
        "tour_days": 4,
        "tour_option": 14,
        "order": 1
    },
    {
        "tour": 2,
        "tour_days": 4,
        "tour_option": 4,
        "order": 2
    },
    {
        "tour": 2,
        "tour_days": 4,
        "tour_option": 15,
        "order": 3
    },
    {
        "tour": 2,
        "tour_days": 4,
        "tour_option": 16,
        "order": 4
    },
    {
        "tour": 2,
        "tour_days": 4,
        "tour_option": 17,
        "order": 5
    },
    {
        "tour": 2,
        "tour_days": 4,
        "tour_option": 18,
        "order": 6
    }
]



class Command(BaseCommand):
    help = 'Generate fake data for MyModel'


    def handle(self, *args, **kwargs):

        for i in program:
            TourProgram.objects.create(
                tour=Tour.objects.get(pk=i['tour']),
                tour_days=TourDay.objects.get(pk=i['tour_days']),
                tour_option=TourDayOption.objects.get(pk=i['tour_option']),
                order=i['order'],
                is_landmark=False,
                image_url=None
            )

        self.stdout.write(self.style.SUCCESS(f'Successfully generated data entries'))

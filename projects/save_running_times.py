


def main():
    num_videos = int(input('How many vides are in the project? '))
    video_file = open('video_times.text', 'w')

    print('Enter the running time for each video.')
    for count in range(1, num_videos + 1):
        run_time = float(input(f'video#{count}: '))
        video_file.write(f'Video Hours :' + f' {run_time}\n')

    video_file.close()
    print('The times has been saved to vider_times.text. Thank you')

if __name__ == '__main__':
    main()                
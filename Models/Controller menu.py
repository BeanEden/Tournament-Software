from Models.menu import *
from Models.base import *
from Models.players import add_a_player


def main_menu():
    print_main_menu()
    user_input = 0

    while user_input != 5:
        user_input = int(input())
        if user_input == 1:
            tournament_menu()
        elif user_input == 2:
            add_a_player()
            main_menu()
        elif user_input == 3:
            print("Executing menu item 3")
        elif user_input == 4:
            print_consulting_menu()


def tournament_menu():
    print_tournament_menu()
    user_input_tournament_menu = 0
    while user_input_tournament_menu != 3:
        user_input_tournament_menu = int(input())
        if user_input_tournament_menu == 1:
            tournament_created_played = create_a_tournament()
            tournament_round_start_menu(tournament_created_played,1)
        elif user_input_tournament_menu == 2 :
            print("using an already existing")
    main_menu()


# # def consulting_menu():
# #     print_consulting_menu()
# #     user_input_consulting_menu = 0
# #     while user_input_consulting_menu != 4:
# #         user_input_consulting_menu = int(input())
# #         if user_input_consulting_menu == 1:
# #         consulting_tournament_menu()
# #         elif user_input_consulting_menu == 2:
# #         consulting_player_menu()
# #         elif user_input_consulting_menu == 3:
# #         consulting_match_menu()
# #     main_menu()
#
#
# def consulting_tournament_menu():
#     print_consulting_tournament_menu()
#     user_input_consulting_tournament_menu = 0
#     while user_input_consulting_tournament_menu != 4:
# #         user_input_consulting_tournament_menu = int(input())
# #         if user_input_consulting_tournament_menu == 1:
# #
# #         elif user_input_consulting_tournament_menu == 2:
# #
# #         elif user_input_consulting_tournament_menu == 3:
# #         print_consulting_menu()
# #     main_menu()
#
#
# def consulting_player_menu():
#     print_consulting_player_menu()
#     user_input_consulting_player_menu = 0
#     while user_input_consulting_player_menu != 4:
# #         user_input_consulting_player_menu = int(input())
# #         if user_input_consulting_player_menu == 1:
# #
# #         elif user_input_consulting_player_menu == 2:
# #
# #         elif user_input_consulting_player_menu == 3:
# #         print_consulting_menu()
# #     main_menu()
#
#
# def consulting_match_menu():
#     print_consulting_match_menu()
#     user_input_consulting_match_menu = 0
#     while user_input_consulting_match_menu != 4:
#         user_input_consulting_match_menu = int(input())
#         if user_input_consulting_match_menu == 1:
#
#         elif user_input_consulting_match_menu == 2:
#
#         elif user_input_consulting_match_menu == 3:
#         print_consulting_menu()
#     main_menu()
# while round_count < tourn
def tournament_round_start_menu(tournament, round_count):
    print_tournament_round_start_menu(round_count)
    user_input_tournament_round_start_menu = 0
    player_list = tournament.player_list_tournament()
    while user_input_tournament_round_start_menu != 5:

        if user_input_tournament_round_start_menu == 1 and round_count == 1:
            round_one = round_one_run_function(player_list)
            tournament.append(round_one)
            round_menu(round_one, round_count)
        elif user_input_tournament_round_start_menu == 1 and round_count != 1:
            round_played = secondary_round_run_function(player_list, round_count)
            tournament.append(round_played)
            round_menu(round_played, round_count)
        elif user_input_tournament_round_start_menu == 2:
            print(player_list)
        elif user_input_tournament_round_start_menu == 3:
            print(tournament)
        elif user_input_tournament_round_start_menu == 4:
            print(tournament)
    main_menu()

def round_menu(round, round_count):
    round_status = round.status
    print_round_menu(round_count,round_status)
    user_input_round_menu = 0

    while user_input_round_menu != 5:
        user_input_round_menu= int(input())
        if user_input_round_menu == 1 and round_status == "open":
        print(round.matches_list)
        elif user_input_round_menu == 1 and round_status != "open" :
        print(round.matches_list)
        elif user_input_round_menu == 2:
            select_a_match_for_result()
        elif user_input_round_menu == 3:
        elif user_input_round_menu == 4:
    main_menu()

def select_a_match_for_result(round_count, matches_list):
    print_select_a_match_for_result()
    user_input_select_a_match_for_result = 0
    while user_input_select_a_match_for_result != 5:
        user_input_select_a_match_for_result= int(input())
        if user_input_select_a_match_for_result == 1:
            enter_match_result(matches_list[0])
        elif user_input_select_a_match_for_result == 2:
            enter_match_result(matches_list[1])
        elif user_input_select_a_match_for_result == 3:
            enter_match_result(matches_list[2])
        elif user_input_select_a_match_for_result == 4:
            enter_match_result(matches_list[3])
    round_menu()

def enter_match_result(match)
    print_enter_match_result()
    user_input_enter_match_result = 0
    while user_input_enter_match_result != 4:
        user_input_round_menu = int(input())
        if user_input_round_menu == 1:
            match.score_attribution(1)
            user_input_enter_match_result = 4
        elif user_input_round_menu == 2:
            match.score_attribution(2)
            user_input_enter_match_result = 4
        elif user_input_round_menu == 3:
            match.score_attribution(3)
            user_input_enter_match_result = 4
    select_a_match_for_result()
# main_menu()
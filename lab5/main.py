from numpy import std


from accuracy import Accuracy
from draw_graphic import drawGraphic
from integration import Analytical, MonteCarloFirst, MonteCarloSecond, Trapezium


def main():
    drawGraphic()
    trapezium = Accuracy.investigate_num_of_nodes_to_1_percent_accuracy(Trapezium.count)
    monte_carlo_first = Accuracy.investigate_num_of_nodes_to_1_percent_accuracy(MonteCarloFirst.count)
    monte_carlo_second = Accuracy.investigate_num_of_nodes_to_1_percent_accuracy(MonteCarloSecond.count)

    print('Number of nodes for getting 1 percent accuracy for each method.')
    print("----------------------------------------------------------------------")
    print("Number of nodes of " + str(Trapezium()) + ": " + str(trapezium))
    print("Number of nodes of " + str(MonteCarloFirst()) + ": " + str(monte_carlo_first))
    print("Number of nodes of " + str(MonteCarloSecond()) + ": " + str(monte_carlo_second))
    print("----------------------------------------------------------------------")
    print('Analytic count: ' + str(round(Analytical.count(), 3)))
    print('Trapezium method count: ' + str(round(Trapezium.count(trapezium), 3)))
    print('Monte-Carlo 1st method count: ' + str(round(MonteCarloFirst.count(monte_carlo_first), 3)))
    print('Monte-Carlo 2nd method count: ' + str(round(MonteCarloSecond.count(monte_carlo_second), 3)))
    print()
    print('Standard deviation for 1st method' + ": " +
          str(round(std([MonteCarloFirst.count(monte_carlo_first) for _ in range(100)]), 3)))
    print('Standard deviation for 2nd method' + ": " +
          str(round(std([MonteCarloSecond.count(monte_carlo_second) for _ in range(100)]), 3)))




if __name__ == '__main__':
    main()

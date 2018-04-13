import ParameterClasses as P
import MarkovModel as MarkovCls
import SupportMarkovModel as SupportMarkov

# create and cohort
cohort1 = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.NONE)

simOutputs_none = cohort1.simulate()


# create and cohort
cohort2 = MarkovCls.Cohort(
    id=1,
    therapy=P.Therapies.ANTICOAG)

simOutputs_anticoag = cohort2.simulate()

SupportMarkov.print_comparative_outcomes(simOutputs_none=simOutputs_none,simOutputs_anticoag=simOutputs_anticoag)


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

SupportMarkov.report_CEA_CBA(simOutputs_none, simOutputs_anticoag)

print('Anticoagulation therapy is recommended when willingness to pay is above approximately $21,000')

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

def get_summary(text):
    language = "english"
    sentence_count = 5
    parser = PlaintextParser(text, Tokenizer(language))
    summarizer_2 = LsaSummarizer(Stemmer(language))
    summarizer_2.stop_words = get_stop_words(language)
    summary_2 = summarizer_2(parser.document, sentence_count)
    print(summary_2)
    # for sentence in summary_2:
    #     print(sentence)

if __name__ == '__main__':
    get_summary("""
    Background

In 1961, United States President John F. Kennedy challenged his nation to land an astronaut on the Moon by the end of the decade, with a safe return to Earth.[3] After considerable debate, NASA (the US government's spaceflight agency) decided in late 1962 that lunar missions would use a lunar orbit rendezvous in which the complete Apollo spacecraft would be propelled towards lunar orbit by the Saturn V launch vehicle's third stage (called the S-IVB). Once in lunar orbit, those astronauts who would land on the Moon would enter what was then called the lunar excursion module (LEM) (later called the lunar module (LM)). This craft would separate from the Apollo's command and service module (CSM) and land on the Moon. When the astronauts were ready to return, they would enter the LM, take off, and re-dock with the CSM. Once the crew reentered the CSM, they would discard the lunar module and return to Earth in the CSM.[4] In 1962, NASA invited eleven companies to bid for the contract to construct the LM. On November 7, 1962, NASA announced that it had awarded the contract to Grumman in Bethpage, New York.[5]
Delays

As with Apollo 4, there were significant delays for Apollo 5. The primary cause of the Apollo 5 delays was the LM, which was behind schedule. Apollo Program Manager Major General Samuel C. Phillips had originally hoped that the uncrewed test flight of LM-1, the first lunar module, would launch in April 1967. Anticipating six months for checkout and testing of the vehicle, NASA asked Grumman to have LM-1 delivered to Kennedy Space Center in Florida by September 1966, but due to difficulties in manufacturing LM-1, delivery was repeatedly delayed. The delivery date was still uncertain when AS-206, the Saturn IB launch vehicle planned to boost LM-1 to orbit, was erected at Launch Complex 37 in January 1967. After the fire that month that killed the Apollo 1 crew, the launch vehicle planned for Apollo 1, AS-204, was moved from Launch Complex 34 to Launch Complex 37 and replaced AS-206.[6] This was done because AS-204 was the last Saturn IB with full research and development instrumentation, and, with crewed flight on hold, NASA wanted to use that booster for the first flight of the LM.[7][a]

With no LM yet available, Grumman built a plywood mockup of one at Launch Complex 37 to aid in facilities verification.[9] On May 12, 1967, Apollo Program Spacecraft Manager George M. Low informed NASA headquarters that Grumman was committed to a June 28 delivery of LM-1, though Low noted that the goal would be hard to meet.[10] On June 23, LM-1 arrived at Cape Kennedy on board Aero Spacelines' Super Guppy; the stages were mated to each other four days later.[9][11] A 400-person team under John J. Williams, a veteran of launch operations for both Mercury and Gemini, checked to see that LM-1 met specifications, after which they supervised Grumman technicians, who tested and modified the vehicle.[11] Due to leaks in the LM's ascent stage, the two stages were demated in August, and after these were fixed and the stages remated, another leak developed and the stages were demated again in September. During this time, several pieces of equipment were removed for repair by Grumman; the stages were remated again in October.[9]

As of September 6, 1967, Apollo 5 was running about 39 days behind the plan established on July 18, but all known issues were being dealt with, with the exception of some leaks from the propulsion system.[12] Most mission documents were ready by late 1967; Mission Director William C. Schneider issued mission rules on November 18, 1967. The following day, LM-1 was mated to its launch vehicle, and the space vehicle readiness test was completed in December. In early January 1968, the office of NASA Administrator James E. Webb announced that Apollo 5 would be launched no earlier than January 18, 1968. Minor faults such as clogged filters led to some additional delays. The countdown demonstration test concluded on January 19 and an abbreviated 22-hour countdown began on January 21.[13][14]
Objectives
A large plane has opened to show its interior, in which there is a huge packing crate (LM-1)
LM-1 is delivered by Super Guppy aircraft, June 23, 1967

Apollo 5 was intended to verify the operation of the subsystems of the LM. During the flight, the ascent and descent engines would be fired. A "fire in the hole" test would be conducted to verify that the ascent stage could still fire while attached to the descent stage, a procedure that would be used on the lunar surface and in the event of an aborted lunar landing. It involved shutting down the descent stage, switching control and power to the ascent stage, and starting the ascent engine while the two stages were still mated. The term "fire in the hole" derived from a term used in mining when explosives are about to be used.[13][15][16] Additional testing was to check that the LM engines could be restarted after initial use.[17] In addition to testing LM systems, Apollo 5 was to test the Instrument Unit in its Saturn V configuration.[9]

It was expected that the ascent stage of LM-1 would remain in orbit for about two years before re-entering the atmosphere and disintegrating, and the descent stage for about three weeks.[18]
Equipment
A rocket sits on a launchpad
Apollo 5's Saturn IB on the launchpad

Apollo 5 was launched into orbit by the Saturn IB, designated SA-204R, which had been assigned to Apollo 1. Originally brought to Cape Kennedy in August 1966, it had survived the fire unscathed, having been inspected after the fire for corrosion or other damage.[9][11][19] Ignition weight for the launch vehicle, including the spacecraft and propellant, was 589,413 kilograms (1,299,434 lb).[20]

The space vehicle for this mission was 55 meters (180 ft) tall, but had a stubby appearance since it had neither a CSM nor a launch escape system. Instead, the LM was housed within the spacecraft-lunar module adapter (SLA) at the top of the vehicle stack.[11] The SLA, numbered as SLA-7,[21] was just below the nose cap in the stack, and had four panels that would open once the nose cap was jettisoned in orbit, allowing the LM room to separate and move away.[22]

The LM, designated as LM-1, was the first flight-ready Apollo lunar module. To save weight, and because they would not be necessary during the test mission, LM-1 had no landing legs.[23]

After one of the windows of LM-5 (which would fly on Apollo 11) broke during testing in December 1967, NASA officials decided to replace the windows of LM-1 with aluminum plates out of concern a window might fail in flight.[24] Since there would be no astronauts aboard, LM-1 had a mission programmer installed, which could control the craft remotely.[25] Not all LM-1 systems were fully activated nor was it given a full load of consumables: for example, its primary batteries were partially discharged to avoid over-voltage complications, and the oxygen tanks for the environmental control systems were only partially full.[26]
Flight

On January 22, 1968, Apollo 5 lifted off from Launch Complex 37B at Cape Kennedy Air Force Station[23] at 17:48:08 Eastern Standard Time (22:48:08 UTC).[9] The Saturn IB worked perfectly, inserting the second stage and LM into a 88-by-120-nautical-mile (163 by 222 km) orbit.[1][b] The nose cone was jettisoned, and after a coast of 43 minutes 52 seconds, the LM separated from its adapter, in a 90-by-120-nautical-mile (167 by 222 km) orbit.[1]

After two orbits, the first planned 39-second descent-engine burn was started, but this was aborted after only four seconds by the Apollo Guidance Computer, which detected that the spacecraft was not going as fast as expected. This happened because one of the engine's valves was suspected of being leaky and was not armed until it was time to ignite the engine, in orbit, which meant that the propellant took longer to reach the engine, leading to the lag. Programmers could have adjusted the software to account for this, but were not told. In addition, the tanks were only half full, and this contributed to the slowness of the ship. Had this occurred on a crewed mission, the astronauts would have been able to analyze the situation and decide whether the engine should be restarted.[13][27]
Two middle-aged men sit at consoles, wearing headsets
Director of Flight Operations Christopher C. Kraft (left) and Manned Spaceflight Center director Robert R. Gilruth in Mission Control during Apollo 5

Gene Kranz was the flight director for Apollo 5.[16] Mission Control, under Kranz's command, decided on a plan to conduct the engine and "fire-in-the-hole" tests under manual control. There were communication problems with the spacecraft, and omitting these tests would have meant the mission was a failure. Despite this, Kranz's team accomplished every burn.[28] The ascent stage spun out of control eight hours into the mission, after completion of the engine burns, due to a problem with the guidance system.[29]

The stages were left in a low enough orbit that atmospheric drag would soon cause their orbits to decay and re-enter the atmosphere. The ascent stage re-entered on January 24 and burned up; the descent stage re-entered on February 12, falling into the Pacific several hundred miles southwest of Guam.[30][31] Simulations showed that the S-IVB stage of the launch vehicle (1968-007B) re-entered about 15.5 hours into the flight.[32]

Apollo Spacecraft Program Manager George M. Low said that Apollo 5's success "was due to the fact that we had a good piece of hardware; it was due to the fact that we had outstanding flight control teams under Gene Kranz' able leadership."[23] Despite the trouble during the descent-engine burn, NASA deemed the mission a success in demonstrating the LM systems, and a second uncrewed flight test using LM-2 was cancelled.[32] The first crewed LM flight took place on Apollo 9 in March 1969.[33] """)
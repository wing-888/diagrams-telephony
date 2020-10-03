from diagrams import Diagram, Cluster

from telephony import *

with Diagram('Examples', show=False, direction='TB'):
    with Cluster('VoIP'):
        with Cluster('Media Proxies'):
            rtpengine = RTPEngine('RTPEngine')

        with Cluster('Other'):
            freeradius = FreeRADIUS('FreeRADIUS')
            freediameter = FreeDiameter('FreeDiameter')

        with Cluster('Telephony engines'):
            asterisk = Asterisk('Asterisk')
            opensips = OpenSIPS('OpenSIPS')
            freeswitch = FreeSWITCH('FreeSWITCH')
            kamailio = Kamailio('Kamailio')
            yate = Yate('Yate')
            sipxecs = SipXecs('SipXecs')

            sipxecs >> freeswitch

            with Cluster('Unified Communications Server'):
                sipxcom = SipXcom('SipXcom')

                issabel = Issabel('Issabel')
                issabel >> asterisk

                elastix = Elastix('Elastix')
                elastix >> asterisk

        with Cluster('PBX systems'):
            freepbx = FreePBX('FreePBX')
            freepbx >> asterisk
            elastix >> freepbx

            mikopbx = MikoPBX('MikoPBX')
            mikopbx >> asterisk

            fusionpbx = FusionPBX('FusionPBX')
            fusionpbx >> freeswitch

    with Cluster('Communication devices'):
        soft_phone = SoftPhone('SoftPhone')
        cellphone = CellPhone('CellPhone')
        smartphone = SmartPhone('SmartPhone')
        landline_phone = LandLinePhone('LandLinePhone')

        fax = Fax('Fax')

    with Cluster('Other'):
        satellite = Satellite('Satellite')
        dish_antenna = DishAntenna('DishAntenna')

        satellite >> dish_antenna

        sip_protocol = SipProtocol('SipProtocol')

        walkie_talkie = WalkieTalkie('WalkieTalkie')
        communication_tower = CommunicationTower('CommunicationTower')
        call_center_operator = CallCenterOperator('CallCenterOperator')

        voicemail = VoiceMail('VoiceMail')

        call_talking = CallTalking('CallTalking')

        person_1 = VideoTalking('VideoTalking')
        person_2 = VideoTalking('VideoTalking')

        person_1 >> sip_protocol >> person_2
        person_2 >> sip_protocol >> person_1

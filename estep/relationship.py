import logging
import six

LOGGER = logging.getLogger('estep')

relationships = [
    ('http://software.esciencecenter.nl/schema/software', 'usedIn', 'http://software.esciencecenter.nl/schema/project', 'uses'),
    ('http://software.esciencecenter.nl/schema/software', 'dependency',
     'http://software.esciencecenter.nl/schema/software', 'dependencyOf'),
    # FIXME person:contactPerson is for project only? so below not OK?
    ('http://software.esciencecenter.nl/schema/software',
                                                      'contactPerson',
                                                      'http://software.esciencecenter.nl/schema/person',
                                                      'contactPersonOf'),
    ('http://software.esciencecenter.nl/schema/software',
                                                      'owner',
                                                      'http://software.esciencecenter.nl/schema/person',
                                                      'ownerOf'),
    ('http://software.esciencecenter.nl/schema/software',
                                                      'owner',
                                                      'http://software.esciencecenter.nl/schema/organization',
                                                      'ownerOf'),
    ('http://software.esciencecenter.nl/schema/software',
                                                      'user',
                                                      'http://software.esciencecenter.nl/schema/person',
                                                      'userOf'),
    ('http://software.esciencecenter.nl/schema/software',
                                                      'user',
                                                      'http://software.esciencecenter.nl/schema/organization',
                                                      'userOf'),
    ('http://software.esciencecenter.nl/schema/software',
                                                      'contributor',
                                                      'http://software.esciencecenter.nl/schema/person',
                                                      'contributorOf'),
    ('http://software.esciencecenter.nl/schema/project',
                                                      'contactPerson',
                                                      'http://software.esciencecenter.nl/schema/person',
                                                      'contactPersonOf'),
    ('http://software.esciencecenter.nl/schema/project',
                                                      'coordinator',
                                                      'http://software.esciencecenter.nl/schema/person',
                                                      'coordinatorOf'),
    ('http://software.esciencecenter.nl/schema/project',
                                                      'engineer',
                                                      'http://software.esciencecenter.nl/schema/person',
                                                      'engineerOf'),
    ('http://software.esciencecenter.nl/schema/project',
                                                      'principalInvestigator',
                                                      'http://software.esciencecenter.nl/schema/person',
                                                      'principalInvestigatorOf'),
    # FIXME software:involvedOrganization has no counterpart in organization schema
    # From project
    ('http://software.esciencecenter.nl/schema/project',
                                                  'involvedOrganization',
                                                  'http://software.esciencecenter.nl/schema/organization',
                                                  'involvedIn'),
]

def get_validators():
    return [RelationshipValidator(*r) for r in relationships]



class AbstractValidator(object):
    def validate(self, name, instance):
        # TODO yield errors instead of logging errors and returning nr_errors
        raise NotImplementedError

    def finalize(self):
        # TODO yield errors instead of logging errors and returning nr_errors
        return 0


class RelationshipValidator(AbstractValidator):
    """

    >>> validator = RelationShipValidator('http://software.esciencecenter.nl/schema/software', 'usedIn',
    ...                                   'http://software.esciencecenter.nl/schema/project', 'uses')
    >>> validator.validate('twinl', {'schema': 'http://software.esciencecenter.nl/schema/project',
    ...                              '@id': 'http://software.esciencecenter.nl/project/twinl',
    ...                              'uses': ['http://software.esciencecenter.nl/software/twiqs.nl']})
    ... # twinl uses twiqs.nl, but twiqs.nl has not been seen yet, so OK for now
    0
    >>> validator.validate('twiqs.nl', {'schema': 'http://software.esciencecenter.nl/schema/software',
    ...                                 '@id': 'http://software.esciencecenter.nl/software/twiqs.nl',
    ...                                 'usedIn': ['http://software.esciencecenter.nl/project/twinl']})
    ... # twiqs.nl is used in twinl and twinl uses twiqs.nl, so is OK
    0
    >>> validator.validate('emetabolomics', {'schema': 'http://software.esciencecenter.nl/schema/project',
    ...                                      '@id': 'http://software.esciencecenter.nl/project/emetabolomics',
    ...                                      'uses': ['http://software.esciencecenter.nl/software/xenon']})
    ... # xenon is used by emetabolomics, but xenon has not been seen yet, so OK for now
    0
    >>> validator.validate('xenon', {'schema': 'http://software.esciencecenter.nl/schema/software',
    ...                              '@id': 'http://software.esciencecenter.nl/software/xenon',
    ...                              'usedIn': ['http://software.esciencecenter.nl/project/simcity']})
    ... # xenon is used by emetabolomics, but xenon is not used in emetabolomics, so gives error
    1
    >>> validator.validate('simcity', {'schema': 'http://software.esciencecenter.nl/schema/project',
    ...                                '@id': 'http://software.esciencecenter.nl/project/simcity',
    ...                                'uses': ['http://software.esciencecenter.nl/software/pyxenon']})
    ... # xenon is used in simcity, but simcity does not use xenon, so gives error
    1
    >>> validator.finalize()
    ... # simcity uses pyxenon, but validator has not seen pyxenon, so gives error
    1

    """
    def __init__(self, schema1, prop1, schema2, prop2):
        self.schema1 = schema1
        self.prop1 = prop1
        self.memory1 = {}
        self.schema2 = schema2
        self.prop2 = prop2
        self.memory2 = {}
        self.errors = set()

    def validate(self, name, instance):
        schema = instance['schema']
        myid = instance['@id']
        nr_errors = 0

        if schema == self.schema1 and self.prop1 in instance:
            if isinstance(instance[self.prop1], str):
                myvalues = set([instance[self.prop1]])
            elif isinstance(instance[self.prop1], dict):
                # not a @id
                return nr_errors
            else:
                myvalues = set([d for d in instance[self.prop1] if isinstance(d, str)])

            for myvalue in myvalues:
                if myvalue not in self.memory2:
                    LOGGER.debug('Unable to validate {0} {1} {2}, have not seen counterpart yet'.format(myid, self.prop1, myvalue))
                    continue
                if myid in self.memory2[myvalue]:
                    LOGGER.debug('{0} {1} {2} and {2} {3} {0}'.format(myid, self.prop1, myvalue, self.prop2))
                    continue
                error = 'Missing "{0}"'.format(myid)
                LOGGER.warning('* Error      : ' + error)
                LOGGER.warning('  On property: ' + self.prop2 + ' of ' + myvalue)
                self.errors.add((myid, self.prop2, myvalue))
                nr_errors += 1

            # find other direction
            for otherid, othervalues in six.iteritems(self.memory2):
                if myid in othervalues and otherid not in myvalues:
                    error = 'Missing "{0}"'.format(otherid)
                    LOGGER.warning('* Error      : ' + error)
                    LOGGER.warning('  On property: ' + self.prop1)
                    self.errors.add((otherid, self.prop1, myid))
                    nr_errors += 1

            self.memory1[myid] = myvalues
        if schema == self.schema2 and self.prop2 in instance:
            if isinstance(instance[self.prop2], str):
                myvalues = set([instance[self.prop2]])
            elif isinstance(instance[self.prop2], dict):
                # not a @id
                return nr_errors
            else:
                myvalues = set([d for d in instance[self.prop2] if isinstance(d, str)])

            for myvalue in myvalues:
                if myvalue not in self.memory1:
                    LOGGER.debug('Unable to validate {0} {1} {2}, have not seen counterpart yet'.format(myid, self.prop2, myvalue))
                    continue
                if myid in self.memory1[myvalue]:
                    LOGGER.debug('{0} {1} {2} and {2} {3} {0}'.format(myid, self.prop2, myvalue, self.prop1))
                    continue
                error = 'Missing "{0}"'.format(myid)
                LOGGER.warning('* Error      : ' + error)
                LOGGER.warning('  On property: ' + self.prop1 + ' of ' + myvalue)
                self.errors.add((myid, self.prop1, myvalue))
                nr_errors += 1

            # find other direction
            for otherid, othervalues in six.iteritems(self.memory1):
                if myid in othervalues and otherid not in myvalues:
                    error = 'Missing "{0}"'.format(otherid)
                    LOGGER.warning('* Error      : ' + error)
                    LOGGER.warning('  On property: ' + self.prop2)
                    self.errors.add((otherid, self.prop2, myid))
                    nr_errors += 1

            self.memory2[myid] = myvalues

        return nr_errors

    def missing(self):
        for myid, myvalues in six.iteritems(self.memory1):
            for myvalue in myvalues:
                if myvalue in self.memory2 and myid in self.memory2[myvalue]:
                    pass
                else:
                    LOGGER.info("* Found missing relationship {0}#{1} to {2}".format(myid, self.prop2, myvalue))
                    yield (myid, self.prop2, myvalue)

        for myid, myvalues in six.iteritems(self.memory2):
            for myvalue in myvalues:
                if myvalue in self.memory1 and myid in self.memory1[myvalue]:
                    pass
                else:
                    LOGGER.info("* Found missing relationship {0}#{1}: {2}".format(myid, self.prop1, myvalue))
                    yield (myid, self.prop1, myvalue)

    def finalize(self):
        nr_errors = 0
        for myid, myvalues in six.iteritems(self.memory1):
            for myvalue in myvalues:
                if myvalue in self.memory2 and myid in self.memory2[myvalue]:
                    pass
                else:
                    error = 'Missing "{0}"'.format(myid)
                    if (myid, self.prop2, myvalue) not in self.errors:
                        LOGGER.warning('* Error      : ' + error)
                        LOGGER.warning('  On property: ' + self.prop2 + ' of ' + myvalue)
                        nr_errors += 1

        for myid, myvalues in six.iteritems(self.memory2):
            for myvalue in myvalues:
                if myvalue in self.memory1 and myid in self.memory1[myvalue]:
                    pass
                else:
                    # error = '"{0}" not found locally'.format(myvalue)
                    error = 'Missing "{0}"'.format(myid)
                    if (myid, self.prop1, myvalue) not in self.errors:
                        LOGGER.warning('* Error      : ' + error)
                        LOGGER.warning('  On property: ' + self.prop1 + ' of ' + myvalue)
                        nr_errors += 1

        return nr_errors

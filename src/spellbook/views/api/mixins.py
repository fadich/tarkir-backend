from collections import defaultdict


class SchoolFormatterMixin:

    @classmethod
    def reformat_school(cls, school: dict):
        spells = defaultdict(list)

        school['passive_bonuses'] = {
            f'{school["shortcut"]}{link["passive_bonus"]["cycle"]}': {
                **link['passive_bonus'],
                'schools': [ll['school'] for ll in link['passive_bonus']['schools']]
            }
            for link in school['passive_bonuses']
        }

        for spell in school['spells']:
            spell['spell']['schools'] = [
                {
                    'cycle': school['cycle'],
                    **school['school'],
                } for school in spell['spell']['schools']
            ]

            spell = {
                'cycle': spell['cycle'],
                **spell['spell'],
            }

            spells[f'{school["shortcut"]}{spell["cycle"]}'].append(spell)

        return {
            **school,
            'spells': spells,
        }

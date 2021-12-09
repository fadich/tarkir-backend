from collections import defaultdict


class SchoolFormatterMixin:

    @classmethod
    def reformat_school(cls, school: dict):
        spells = defaultdict(list)
        passive_bonuses = defaultdict(list)

        for link in school['passive_bonuses']:
            link['passive_bonus']['schools'] = [s['school'] for s in link['passive_bonus']['schools']]

            passive_bonuses[f'{school["shortcut"]}{link["passive_bonus"]["cycle"]}'].append({
                **link['passive_bonus']
            })

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
            'passive_bonuses': passive_bonuses,
        }

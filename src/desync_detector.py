import base64
import zlib
from pprint import pprint
from typing import Iterable

from replay_parser.replay_parser import parse

from base.robot import Base
from config import REPLAY_DIR
from utils.paths import get_dir_path


class DesyncDetector(Base):
    def get_data(self) -> Iterable:
        self.db_con.query("""
            SELECT `game_player_stats`.`gameId`, GROUP_CONCAT(`login`.`login`)
            FROM `game_player_stats`
            INNER JOIN `login` ON `login`.`id` = `game_player_stats`.`playerId`
            WHERE `gameId` = '6176549'
            GROUP BY `game_player_stats`.`gameId`
            ORDER BY `game_player_stats`.`id` DESC
            LIMIT 4
        """)
        result = self.db_con.store_result()
        row = result.fetch_row()
        while row:
            yield row
            row = result.fetch_row()

    def process_data(self, data) -> None:
        game_id, usernames = data[0]
        usernames = usernames.decode().split(",")

        print(game_id, usernames)
        file_path = get_dir_path(REPLAY_DIR, int(game_id), "scfareplay")

        with open(file_path, "rb") as f:
            # f.readline()  # json
            replay_data = f.read().strip()
            # replay_data = zlib.decompress(base64.b64decode(replay_data)[4:])
            result = parse(replay_data, parse_until_destync=True)
            pprint(result['desync_ticks'])
            print("\n")


        # 1. najdi replay
        # 2. otkroj
        # 3. replay_parser
        # 4. desync time
        # 5. replay time
        # 6. get players from replay
        # 7. get nicknames from server
        # 8. compare
        # 9. notify if differ
        # 10. exause us for maj bad inglish


if __name__ == "__main__":
    DesyncDetector().run()

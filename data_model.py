from sqlalchemy import Column, Integer, TEXT, DATETIME, BOOLEAN, VARCHAR, FLOAT
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class VideoSearch60Content(Base):
	__tablename__ = 't_video_speech_to_text'
	sid = Column(Integer)
	video_id = Column(Integer)
	content = Column(TEXT)


class VideoSearch60Content(Base):
	__tablename__ = 't_video_search_60'
	video_id = Column(Integer)
	search_keyword = Column(VARCHAR(20))
	title = Column(VARCHAR(50))
	content = Column(TEXT)
	publish_time = Column(DATETIME)
	duration = Column(Integer)
	author_id = Column(Integer)
	author_name = Column(VARCHAR(20))
	fav_count = Column(Integer)
	unique_flag = Column(Integer)
	tags = Column(TEXT)
	video_url = Column(TEXT)



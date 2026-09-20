from typing import Any
from collections.abc import Callable

from direct.directnotify.DirectNotify import DirectNotify
from direct.showbase.BulletinBoard import BulletinBoard
from direct.showbase.EventManager import EventManager
from direct.showbase.JobManager import JobManager
from direct.showbase.Messenger import Messenger
from direct.task.Task import TaskManager
from panda3d.core import ClockObject, NodePath, VirtualFileSystem
from panda3d.core import ostream as NotifyOStream

from otp.ai.AIBase import AIBase
from toontown.chat.TTChatInputWhiteList import TTChatInputWhiteList
from toontown.chat.TTTalkAssistant import TTTalkAssistant
from toontown.chat.TTWhiteList import TTWhiteList
from toontown.distributed.ToontownClientRepository import ToontownClientRepository
from toontown.launcher.ToontownLauncher import ToontownLauncher
from toontown.toon.LocalToon import LocalToon
from toontown.toonbase.ToonBase import ToonBase
from toontown.toonbase.ToontownLoader import ToontownLoader


class _Game:
    name: str
    process: str


class _ClientBase(ToonBase):
    cr: ToontownClientRepository
    localAvatar: LocalToon
    talkAssistant: TTTalkAssistant
    whiteList: TTWhiteList | None
    ttwl: TTChatInputWhiteList


base: _ClientBase
simbase: AIBase
uber: AIBase
launcher: ToontownLauncher
game: _Game
loader: ToontownLoader
messenger: Messenger
taskMgr: TaskManager
jobMgr: JobManager
eventMgr: EventManager
directNotify: DirectNotify
bboard: BulletinBoard
render: NodePath
render2d: NodePath
aspect2d: NodePath
pixel2d: NodePath
hidden: NodePath
camera: NodePath
globalClock: ClockObject
vfs: VirtualFileSystem | None
ostream: NotifyOStream
run: Callable[..., None]
localAvatar: LocalToon
inspect: Callable[..., Any]
__dev__: bool
__astron__: bool
__execWarnings__: bool

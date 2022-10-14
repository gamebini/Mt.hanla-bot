from audioop import add
import imp
from pydoc import visiblename
from random import choices
from secrets import choice
from tokenize import group
from urllib import response
import discord
from discord import Guild, app_commands
from discord.utils import get
from typing import List
from numpy import blackman
import datetime
from datetime import date, timedelta
from discord.ui import Button, View
from pytz import HOUR

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents = discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        print(f'{self.user}이 시작되었습니다')  #  봇이 시작하였을때 터미널에 뜨는 말
        game = discord.Game('테스트')          # ~~ 하는중
        await self.change_presence(status=discord.Status.idle, activity=game)

        # ch = client.get_channel(1007193771852714064)
        # embed = discord.Embed(title="한라산부대 규정", description="ㅤ", color=0x4000FF)  # 문의 보낸 후 결과 임베드
        # embed.add_field(name="비속어", value="비속어의 경우 어느정도 허용하지만 수위가 높은 발언, 가족에 대한 모욕 등은 일절 금지됩니다. 또한, 욕설을 지나치게 과도 사용하는것도 재제 대상입니다.", inline=False)
        # embed.add_field(name="하극상", value="하극상이란 본인보다 상관인 사람을 모욕하는것, 상관에 지위에 도전하는것, 상관 명령에 불복종하는것 모두 포함되며 그 외 사항은 법무부에 판단에 따라 정해집니다. 단, 상관이 규정에 어긋나거나 도덕적으로 그릇된 명령을 내렸을 경우 명령을 복종하지 않아도 처벌을 하지 않습니다.", inline=False)
        # embed.add_field(name="직무유기", value="직무유기는 2주 이상 본인의 업무를 수행하지 않았을 때 해당되는 죄목이며 최소 해임처리의 처벌을 받습니다.", inline=False)
        # embed.add_field(name="분쟁", value="분쟁은 반드시 dm 등 본인들만의 공간에서 논해야 하며 한라산부대, Hostel 내에서 분쟁을 논하여 다른 유저들이 피해를 받을 경우 재제되며, 서버 채팅에서 분쟁을 논한것 만으로도 재제당할수 있습니다.", inline=False)
        # embed.add_field(name="허위 정보", value="허위 정보를 퍼트려 다른 유저가 피해를 입은 경우 __**강한**__ 재제 대상이며 최대 블랙리스트까지 당할 수 있습니다. 또 허위 정보를 퍼트린 것 만으로도 재제조치가 가능합니다.", inline=False)
        # embed.add_field(name="친목", value="친하다는 이유로 서로에게 욕설을 하는 등 규정을 위반한 경우 본래 처벌보다 더한 재제를 받을 수 있습니다.", inline=False)
        # embed.add_field(name="모욕", value="모욕 만으로도 타인에게 명예훼손을 하는 행위이므로 일절 금지되며 모욕으로 인한 피해를 입었을 경우 __**강한**__ 처벌을 받습니다.", inline=False)
        # embed.add_field(name="도배", value="복잡하거나 장문의 메시지 또는 반복적인 메시지를 보내는 행위는 도배로 간주하며 도배도 엄연한 처벌 대상입니다.", inline=False)
        # embed.add_field(name="테러", value="의도 상관 없이 서버 또는 그룹, 게임의 질서를 망치는 등의 행위는 모두 테러이며 이 경우 __**무조건 블랙리스트**__ 대상입니다.", inline=False)
        # embed.add_field(name="더 추가될 수 있으며 규정을 읽지 않아 생기는 불이익은 전부 본인 책임입니다.", value="ㅤ", inline=False)
        # embed.set_footer(text="made by Dev_bini ㅣ 최근 규정 업데이트 날짜 : 2022년 10월 11일") # Ctrl + K + C 하면 주석처리
        # print("규정 업데이트 완료")
        # await ch.send(<@&>embed=embed)


client = aclient()
tree = app_commands.CommandTree(client)

join_guild = client.get_guild(1007186100076429394)
print(join_guild)

@tree.command(name = '문의', description = '봇을 통해 문의를 할 수 있습니다')  # 문의 명령어
async def slash2(interaction: discord.Interaction, 문의: str):  # 옵션


    embed = discord.Embed(title="봇 문의", description="ㅤ", color=0x4000FF)  # 문의 보낸 후 결과 임베드
    embed.add_field(name="봇 문의가 접수되었습니다", value="ㅤ", inline=False)
    embed.add_field(name="문의 내용", value="{}\n".format(문의), inline=False)  # 문의 내용
    embed.add_field(name="ㅤ", value="**▣ 문의 내용에 대한 답장은 관리팀이 확인후\n답장이 오니 기다려 주시면 감사하겠습니다**", inline=False)
    embed.add_field(name="ㅤ", value="- **한라산부대 관리팀** -", inline=False)  # 관리자 이름

    await interaction.response.send_message(embed=embed, ephemeral = True)

    ch = client.get_channel(1026829816730759249)

    embed1 = discord.Embed(title="명령어 사용 감지됨", description="{} 가 <#{}> 에서 /문의 명령어를 사용했습니다.".format(interaction.user.mention, interaction.channel_id), color=0x4000FF)   # 답변 임베드
    await ch.send(embed=embed1)

    users = await client.fetch_user("680379234459582484")   # 문의 온 문의 내용을 DM으로 받을 사람의 ID
    embed = discord.Embed(title="문의 접수 알림", description="ㅤ", color=0x4000FF)  # 문의 보낸 후 결과 임베드
    embed.add_field(name="문의 접수 유저", value="<@{}>[{}]\n".format(interaction.user.id, interaction.user.id), inline=False)  # 문의 내용
    embed.add_field(name="문의 내용", value="{}".format(문의), inline=False)

    await users.send(embed=embed) # 그 사람에게 올 유저 ID와 문의 내용





@tree.command(name = '문의답변', description = '봇을 통해 문의에 답변을 할 수 있습니다') #답변하기
async def slash2(interaction: discord.Interaction, 유저: discord.Member, 답변: str):   # 옵션

    embed1 = discord.Embed(title="문의 답변", description="ㅤ", color=0x4000FF)   # 답변 임베드
    embed1.add_field(name="답변 내용", value="{}".format(답변) , inline=False)

    embed = discord.Embed(title="✅ 답변 성공", description="ㅤ", color=0x4000FF)   # 답변 임베드
    embed.add_field(name = "성공적으로 답변이 전송되었습니다.", value="답변한 문의자 : {}".format(유저.mention), inline=False)



    await interaction.response.send_message(embed=embed)  # 보내졌을시 나오는 확인 이모티콘
    await 유저.send(embed=embed1)


@tree.command(name = '알림', description = '유저에게 알림을 보냅니다.') #답변하기
async def slash2(inter: discord.Interaction, 유저: discord.Member, 알림제목: str, 내용: str):   # 옵션

    embed1 = discord.Embed(title="명령어 사용", description="ㅤ", color=0x4000FF)   # 답변 임베드
    embed1.add_field(name="내용", value="{}".format(내용) , inline=False)

    embed1 = discord.Embed(title="{}".format(알림제목), description="ㅤ", color=0x4000FF)   # 답변 임베드
    embed1.add_field(name="내용", value="{}".format(내용) , inline=False)

    embed = discord.Embed(title="✅ 알림 전송 성공", description="ㅤ", color=0x4000FF)   # 답변 임베드
    embed.add_field(name = "성공적으로 알림이 전송되었습니다.", value="알림 전송 대상자 : {}".format(유저), inline=False)

    ch = client.get_channel(1026829816730759249)

    embed2 = discord.Embed(title="명령어 사용 감지됨", description="{} 가 /알림 명령어를 <#{}> 에서 {} 에게 사용했습니다.".format(inter.user.mention, inter.channel_id, 유저.mention), color=0x4000FF)   # 답변 임베드
    await ch.send(embed=embed2)



    await inter.response.send_message(embed=embed, ephemeral = True)  # 보내졌을시 나오는 확인 이모티콘


    await 유저.send(유저.mention, embed=embed1)

@tree.command(name = '인증확인', description='역할지급을 사용합니다.(관리자 외에 사용 시 처벌받을 수 있습니다.)')
async def slash2(inter: discord.Interaction, 유저: discord.Member, 역할: discord.Role):

    probation = get(inter.guild.roles, id=1023062116128796753)
    probation1 = get(inter.guild.roles, id=1023061861199007865)
    ch = client.get_channel(1026829816730759249)
    adminrole = get(inter.guild.roles, id=1028484614391615538)
    i = adminrole in inter.user.roles
    if i is True:
        embed = discord.Embed(title="명령어 사용 감지됨", description="{} 가 /인증확인 명령어를 <#{}> 에서 {} 에게 사용했습니다.".format(inter.user.mention, inter.channel_id, 유저.mention), color=0x4000FF)   # 답변 임베드
        embed1 = discord.Embed(title="✅ 지급 성공", description="역할지급이 정상적으로 완료되었습니다.", color=0x4000FF)   # 답변 임베드
        await 유저.add_roles(역할)
        await 유저.add_roles(probation)
        await 유저.remove_roles(probation1)
        await ch.send(embed=embed)
        await inter.response.send_message(embed=embed1, ephemeral=True)
    if i is False:
        embed1 = discord.Embed(title="⚠️ 오류", description="권한이 없습니다.", color=0x4000FF)
        await inter.response.send_message(embed=embed1, ephemeral=True)

@tree.command(name = '블랙리스트', description='유저를 블랙리스트에 등록합니다.(디스코드용)')
async def slash2(inter: discord.Interaction, 유저: discord.Member, 사유: str, 강도: str):

    ch = client.get_channel(1026829816730759249)
    blacklist = client.get_channel(1007197891707801603)
    adminrole = get(inter.guild.roles, id=1028484614391615538)
    i = adminrole in inter.user.roles
    day = date.today()
    if i is True:
        embed = discord.Embed(title="명령어 사용 감지됨", description="{} 가 /블랙리스트 명령어를 <#{}> 에서 {} 에게 사용했습니다.\n 사유: {}".format(inter.user.mention, inter.channel_id, 유저.mention, 사유), color=0x4000FF)   # 답변 임베드
        embed1 = discord.Embed(title="✅ 등록 완료", description="블랙리스트 등록이 성공적으로 완료되었습니다.", color=0x4000FF)   # 답변 임베드
        embed2 = discord.Embed(title="블랙리스트 등록", description="블랙리스트 등록일: {}년 {}월 {}일\n등록자: {}\n블랙리스트 해당자: {}\n블랙리스트 수위: {}\n사유: {}".format(day.year, day.month, day.day, inter.user.mention, 유저.mention, 강도, 사유), color=0x4000FF)   # 답변 임베드
        await 유저.ban()
        await ch.send(embed=embed)
        await blacklist.send(embed=embed2)
        await inter.response.send_message(embed=embed1, ephemeral=True)
    if i is False:
        embed1 = discord.Embed(title="⚠️ 오류", description="권한이 없습니다.", color=0x4000FF)
        await inter.response.send_message(embed=embed1, ephemeral=True)

@tree.command(name = '포인트', description='유저의 포인트를 추가하거나 차감합니다.')
async def slash2(inter: discord.Interaction, 유저: discord.Member, 기존포인트: discord.Role, 변경포인트: discord.Role, 사유: str):

    ch = client.get_channel(1026829816730759249)
    pointreport = client.get_channel(1026453250809008168)
    adminrole = get(inter.guild.roles, id=1028484614391615538)
    i = adminrole in inter.user.roles
    day = date.today()
    if i is True:
        embed = discord.Embed(title="명령어 사용 감지됨", description="{} 가 /포인트 명령어를 <#{}> 에서 {} 에게 사용했습니다.\n{} -> {}\n`사유: {}`".format(inter.user.mention, inter.channel_id, 유저.mention, 기존포인트.mention, 변경포인트.mention, 사유), color=0x4000FF)   # 답변 임베드
        embed1 = discord.Embed(title="✅ 지급 완료", description="포인트 지급이 성공적으로 완료되었습니다.", color=0x4000FF)   # 답변 임베드
        embed2 = discord.Embed(title="포인트 지급", description="포인트 지급일: {}년 {}월 {}일\n통지자: {}\n지급 대상자: {}\n{}-> {}\n사유: {}".format(day.year, day.month, day.day, inter.user.mention, 유저.mention, 기존포인트.mention,  변경포인트.mention, 사유), color=0x4000FF)   # 답변 임베드
        val = 기존포인트 in 유저.roles
        if val is True:
            basic = 기존포인트.name
            unbasic = 변경포인트.name
            basicp = basic[7:]
            unbasicp = unbasic[7:]
            await 유저.add_roles(변경포인트)
            await 유저.remove_roles(기존포인트)
            await ch.send(embed=embed)
            if basicp > unbasicp:
                embed1 = discord.Embed(title="✅ 차감 완료", description="포인트 차감이 성공적으로 완료되었습니다.", color=0x4000FF)   # 답변 임베드
                embed2 = discord.Embed(title="포인트 차감", description="포인트 차감일: {}년 {}월 {}일\n통지자: {}\n차감 대상자: {}\n{}-> {}\n사유: {}".format(day.year, day.month, day.day, inter.user.mention, 유저.mention, 기존포인트.mention,  변경포인트.mention, 사유), color=0x4000FF)
            elif unbasicp > basicp:
                embed1 = discord.Embed(title="✅ 지급 완료", description="포인트 지급이 성공적으로 완료되었습니다.", color=0x4000FF)   # 답변 임베드
                embed2 = discord.Embed(title="포인트 지급", description="포인트 지급일: {}년 {}월 {}일\n통지자: {}\n지급 대상자: {}\n{}-> {}\n사유: {}".format(day.year, day.month, day.day, inter.user.mention, 유저.mention, 기존포인트.mention,  변경포인트.mention, 사유), color=0x4000FF)
            if unbasicp >= 10 and unbasicp < 14:
                await 유저.add_roles()
                
            await pointreport.send(embed=embed2)
            await inter.response.send_message(embed=embed1, ephemeral=True)
        if val is False:
            embed1 = discord.Embed(title="⚠️ 오류", description="대상자의 포인트가 기존포인트 옵션과 일치하지 않습니다.", color=0x4000FF)
            await inter.response.send_message(embed=embed1, ephemeral=True)
    if i is False:
        embed1 = discord.Embed(title="⚠️ 오류", description="권한이 없습니다.", color=0x4000FF)
        await inter.response.send_message(embed=embed1, ephemeral=True)

@tree.command(name = '역할공지', description='특정 역할에게만 공지합니다.')
async def slash2(inter: discord.Interaction, 맨션: discord.Role, 제목: str, 내용: str):

    ch = client.get_channel(1026829816730759249)
    noticechannel = client.get_channel(1007187866604015667)
    adminrole = get(inter.guild.roles, id=1028484614391615538)
    i = adminrole in inter.user.roles
    tday = date.today()
    if i is True:
        embed = discord.Embed(title="명령어 사용 감지됨", description="{} 가 /역할공지 명령어를 <#{}> 에서 사용했습니다.\n`맨션 역할 : {}\n``공지 제목: {}`\n`공지 내용: {}`".format(inter.user.mention, inter.channel_id, 맨션, 제목, 내용), color=0x4000FF)   # 답변 임베드
        embed1 = discord.Embed(title="✅ 공지 완료", description="공지 발행이 성공적으로 완료되었습니다.", color=0x4000FF)   # 답변 임베드
        embed2 = discord.Embed(title="{}".format(제목), description="{}".format(내용), color=0x4000FF)   # 답변 임베드
        embed2.set_footer(text = "{}/{}/{} ㅣ 공지 발행자 : {}".format(tday.year, tday.month, tday.day, inter.user.name))
        await ch.send(embed=embed)
        await noticechannel.send(맨션.mention, embed=embed2)
        await inter.response.send_message(embed=embed1, ephemeral=True)
    if i is False:
        embed1 = discord.Embed(title="⚠️ 오류", description="권한이 없습니다.", color=0x4000FF)
        await inter.response.send_message(embed=embed1, ephemeral=True)

@tree.command(name = '전체공지', description='전체 맨션으로 공지합니다.')
async def slash2(inter: discord.Interaction, 제목: str, 내용: str):

    ch = client.get_channel(1026829816730759249)
    noticechannel = client.get_channel(1007187866604015667)
    adminrole = get(inter.guild.roles, id=1028484614391615538)
    i = adminrole in inter.user.roles
    tday = date.today()
    if i is True:
        embed = discord.Embed(title="명령어 사용 감지됨", description="{} 가 /전체공지 명령어를 <#{}> 에서 사용했습니다.\n`공지 제목: {}`\n`공지 내용: {}`".format(inter.user.mention, inter.channel_id, 제목, 내용), color=0x4000FF)   # 답변 임베드
        embed1 = discord.Embed(title="✅ 공지 완료", description="공지 발행이 성공적으로 완료되었습니다.", color=0x4000FF)   # 답변 임베드
        embed2 = discord.Embed(title="{}".format(제목), description="{}".format(내용), color=0x4000FF)   # 답변 임베드
        embed2.set_footer(text = "{}/{}/{} ㅣ 공지 발행자 : {}".format(tday.year, tday.month, tday.day, inter.user.name))
        await ch.send(embed=embed)
        await noticechannel.send('@everyone', embed=embed2)
        await inter.response.send_message(embed=embed1, ephemeral=True)
    if i is False:
        embed1 = discord.Embed(title="⚠️ 오류", description="권한이 없습니다.", color=0x4000FF)
        await inter.response.send_message(embed=embed1, ephemeral=True)

@tree.command(name = '무맨션공지', description='무맨션으로 공지합니다.')
async def slash2(inter: discord.Interaction, 제목: str, 내용: str):

    ch = client.get_channel(1026829816730759249)
    noticechannel = client.get_channel(1007187866604015667)
    adminrole = get(inter.guild.roles, id=1028484614391615538)
    i = adminrole in inter.user.roles
    tday = date.today()
    if i is True:
        embed = discord.Embed(title="명령어 사용 감지됨", description="{} (이)가 /무맨션공지 명령어를 <#{}> 에서 사용했습니다.\n`공지 제목: {}`\n`공지 내용: {}`".format(inter.user.mention, inter.channel_id, 제목, 내용), color=0x4000FF)   # 답변 임베드
        embed1 = discord.Embed(title="✅ 공지 완료", description="공지 발행이 성공적으로 완료되었습니다.", color=0x4000FF)   # 답변 임베드
        embed2 = discord.Embed(title="{}".format(제목), description="{}".format(내용), color=0x4000FF)   # 답변 임베드
        embed2.set_footer(text = "{}/{}/{} ㅣ 공지 발행자 : {}".format(tday.year, tday.month, tday.day, inter.user.name))
        await ch.send(embed=embed)
        await noticechannel.send(embed=embed2)
        await inter.response.send_message(embed=embed1, ephemeral=True)
    if i is False:
        embed1 = discord.Embed(title="⚠️ 오류", description="권한이 없습니다.", color=0x4000FF)
        await inter.response.send_message(embed=embed1, ephemeral=True)

@tree.command(name = '사용금지', description='사용 금지') # 출석체크 수리 필요
async def slash2(inter: discord.Interaction):
    button1 = Button(label="1번 버튼", style = discord.ButtonStyle.green)
    attend = 0
    async def button_callback1(interaction):
        attend = attend + 1
        await attendchannel.edit(embed=embed2)
        embed3 = discord.Embed(title="✅ 출석 완료", description="출석이 완료되었습니다.", color=0x4000FF)
        await inter.response.send_message(embed=embed3, ephemeral=True)
    button1.callback = button_callback1
    view = View()
    view.add_item(button1)
    ch = client.get_channel(1026829816730759249)
    attendchannel = client.get_channel(1007193443954601994)
    adminrole = get(inter.guild.roles, id=1028484614391615538)
    i = False# 원래 i에 이거 넣어야댐 대괄호 빼고 [adminrole in inter.user.roles]
    tday = date.today()
    if i is True:
        embed = discord.Embed(title="명령어 사용 감지됨", description="{} (이)가 /출석체크 명령어를 <#{}> 에서 사용했습니다.".format(inter.user.mention, inter.channel_id), color=0x4000FF)   # 답변 임베드
        embed1 = discord.Embed(title="✅ 출력 완료", description="출석체크 메시지가 성공적으로 출력되었습니다.", color=0x4000FF)   # 답변 임베드
        embed2 = discord.Embed(title="출석체크", description="{}년 {}월 {}일 출석체크입니다.\n 아래 `출석하기` 버튼을 눌러 출석해주세요.".format(tday.year, tday.month, tday.day), color=0x4000FF)   # 답변 임베드
        embed2.set_footer(text = "{}명 출석 ㅣ 출석체크 출력자 : {}".format(attend, inter.user.name))
        await ch.send(embed=embed)
        await attendchannel.send(embed=embed2, view=view)
        await inter.response.send_message(embed=embed1, ephemeral=True)
    if i is False:
        embed1 = discord.Embed(title="⚠️ 오류", description="권한이 없습니다.", color=0x4000FF)
        await inter.response.send_message(embed=embed1, ephemeral=True)

@tree.command(name = '뮤트', description='유저의 채팅권한을 잠시 압수합니다.')
async def slash2(inter: discord.Interaction, 유저: discord.Member, 일: int, 시간: int, 분: int, 사유: str):

    ch = client.get_channel(1026829816730759249)
    adminrole = get(inter.guild.roles, id=1028484614391615538)
    i = adminrole in inter.user.roles
    mutechannel = client.get_channel(1007193443954601994)
    tday = date.today()
    if i is True:
        embed = discord.Embed(title="명령어 사용 감지됨", description="{} (이)가 /뮤트 명령어를 <#{}> 에서 사용했습니다.\n`유저: {}`\n`시간: {}일 {}시간 {}분`\n`사유 : {}`".format(inter.user.mention, inter.channel_id, 유저, 일, 시간, 분, 사유), color=0x4000FF)   # 답변 임베드
        embed1 = discord.Embed(title="✅ 처벌 완료", description="뮤트가 성공적으로 적용되었습니다.", color=0x4000FF)   # 답변 임베드
        embed2 = discord.Embed(title="뮤트 보고서", description="뮤트 보고일: {}년 {}월 {}일\n집행자: {}\n대상자: {}\n시간 : {}일 {}시간 {}분\n사유: {}".format(tday.year, tday.month, tday.day, inter.user.mention, 유저.mention, 일, 시간, 분, 사유), color=0x4000FF)
        await ch.send(embed=embed)
        await inter.response.send_message(embed=embed1, ephemeral=True)
        timetime = timedelta(days = 일, hours = 시간, minutes = 분)
        await 유저.timeout(timetime)
    if i is False:
        embed1 = discord.Embed(title="⚠️ 오류", description="권한이 없습니다.", color=0x4000FF)
        await inter.response.send_message(embed=embed1, ephemeral=True)

@tree.command(name = '언뮤트', description='유저의 채팅권한 압수를 해제합니다.')
async def slash2(inter: discord.Interaction, 유저: discord.Member, 사유: str):

    ch = client.get_channel(1026829816730759249)
    adminrole = get(inter.guild.roles, id=1028484614391615538)
    i = adminrole in inter.user.roles
    tday = date.today()
    if i is True:
        embed = discord.Embed(title="명령어 사용 감지됨", description="{} (이)가 /언뮤트 명령어를 <#{}> 에서 사용했습니다.\n`유저: `{}\n`사유 : {}`".format(inter.user.mention, inter.channel_id, 유저, 사유), color=0x4000FF)   # 답변 임베드
        embed1 = discord.Embed(title="✅ 처벌 완료", description="뮤트가 성공적으로 적용되었습니다.", color=0x4000FF)   # 답변 임베드
        await ch.send(embed=embed)
        await inter.response.send_message(embed=embed1, ephemeral=True)
        timetime = timedelta(days = 0, hours = 0, minutes = 0, seconds = 0)
        await 유저.timeout(timetime)
    if i is False:
        embed1 = discord.Embed(title="⚠️ 오류", description="권한이 없습니다.", color=0x4000FF)
        await inter.response.send_message(embed=embed1, ephemeral=True)








client.run('MTAxOTkxNjU4NTk5OTI4NjI5Mg.GIxh_z.D0348LMf3UC6qQ5yfpqHhiL5nTgNh1gaQRwE68')
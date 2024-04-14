from mountaineer import sideeffect, ControllerBase, RenderBase
from mountaineer.database import DatabaseDependencies
from pydantic import BaseModel
from fastapi import Request, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from intro_to_mountaineer.models.blogpost import BlogPost

class HomeRender(RenderBase):
    posts: list[BlogPost]

class HomeController(ControllerBase):
    url = "/"
    view_path = "/app/home/page.tsx"

    async def render(
        self,
        request: Request,
        session: AsyncSession = Depends(DatabaseDependencies.get_db_session)
    ) -> HomeRender:
        posts = await session.execute(select(BlogPost))

        return HomeRender(
            posts=posts.scalars().all()
        )

    @sideeffect
    async def add_blogpost( self, 
        payload: str,
        session: AsyncSession = Depends(DatabaseDependencies.get_db_session)
    ) -> None:
        new_blogpost = BlogPost(text=payload)
        session.add(new_blogpost)
        await session.commit()